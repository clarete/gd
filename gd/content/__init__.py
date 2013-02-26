# -*- coding: UTF-8 -*-
# Copyright (C) 2011  Governo do Estado do Rio Grande do Sul
#
#   Author: Lincoln de Sousa <lincoln@gg.rs.gov.br>
#   Author: Rodrigo Sebastiao da Rosa <rodrigo-rosa@procergs.rs.gov.br>
#   Author: Thiago Silva <thiago@metareload.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""Module that instantiates our Flask WSGI app and associates all
implemented blueprints in various modules to this app.
"""
import datetime
import gettext
import xmlrpclib
from sqlalchemy.orm.exc import NoResultFound
from flask import Flask, request, render_template, session, \
     redirect, url_for, abort
from flask.ext.cache import Cache

from gd import conf
from gd.auth import is_authenticated, authenticated_user, NobodyHome
from gd.content.wp import wordpress
from gd.content.tweet import get_mayor_last_tweet
from gd.utils import dumps, msg, categoria_contribuicao_text, sendmail
from gd.model import User, ComiteNews, CadastroComite, session as dbsession

from gd.auth.webapp import auth
from gd.auth.fbauth import fbauth
from gd.govpergunta import govpergunta
from gd.govresponde import govresponde
from gd.govescuta import govescuta
from gd.content.videos import videos
from gd.content.balanco import balanco
from gd.content.gallery import gallery
from gd.audience import audience
from gd.admin import admin
from gd.buzz.webapp import buzz
from gd.utils.gravatar import Gravatar
from libthumbor import CryptoURL

app = Flask(__name__)
app.register_blueprint(auth, url_prefix='/auth')
app.register_blueprint(fbauth, url_prefix='/auth/fb')
app.register_blueprint(govpergunta, url_prefix='/govpergunta')
app.register_blueprint(govresponde, url_prefix='/govresponde')
app.register_blueprint(govescuta, url_prefix='/govescuta')
app.register_blueprint(videos, url_prefix='/videos')
app.register_blueprint(gallery, url_prefix='/fotos')
app.register_blueprint(balanco, url_prefix='/balanco')
app.register_blueprint(audience, url_prefix='/audience')
app.register_blueprint(admin, url_prefix='/admin')
app.register_blueprint(buzz, url_prefix='/buzz')

gravatar = Gravatar(app,default='mm')

# Registering a secret key to be able to work with sessions
app.secret_key = conf.SECRET_KEY

# Loading the config variables from our `gd.conf' module
app.config.from_object(conf)

# Gettext setup
app.jinja_env = app.jinja_env.overlay(extensions=['jinja2.ext.i18n'])
app.jinja_env.install_gettext_callables(
    gettext.gettext, gettext.ngettext, newstyle=True)

cache = Cache(app)

@app.errorhandler(403)
def error403(e):
    return render_template('403.html',
        sidebar=wordpress.getSidebar,
    ), 403

@app.errorhandler(404)
def error404(e):
    return render_template('404.html',
        sidebar=wordpress.getSidebar,
    ), 404

@app.errorhandler(500)
def error500(e):
    return render_template('500.html',
        sidebar=wordpress.getSidebar,
    ), 500

@app.errorhandler(502)
def error502(e):
    return render_template('502.html',
        sidebar=wordpress.getSidebar,
    ), 502

def _format_postsearch(posts):
    """" Retorna os campos para ser montado na tela:
        title, url, posttype, data, excerpt, textobotao, thumbs
        Chamar assim na outra pagina:
        for title, url, posttype, txtdata, excerpt, textobotao, thumbs in posts
    """
    title = []
    url = []
    posttype = []
    txtdata = []
    excerpt = []
    textobotao = []
    thumbs = []
    for p in posts:
        if p.post_type == 'audiencia_govesc':
            title.append(p.title)
            aux_date = map(lambda x: x['value'][6:10]+'-'+x['value'][0:2]+'-'+x['value'][3:5]+' '+x['value'][11:13]+':'+x['value'][14:16], filter(lambda x: x['key']  == 'wp_govescuta_data_govesc', p.custom_fields))
            aux_date = formatarDataeHoraPostType(aux_date[0],"%d")+" "+formatarDataeHoraPostType(aux_date[0],"%B").capitalize()+" de "+formatarDataeHoraPostType(aux_date[0],"%Y")
            url.append(url_for('govescuta.govescuta_details', aid=p.id))
            posttype.append(u'Audiências')
            txtdata.append(aux_date)
            excerpt.append(p.excerpt)
            textobotao.append('Veja como foi')
            thumbs.append('')
        elif p.post_type == 'clippinggd_clipping':
            title.append(p.title)
            aux_fonte = map(lambda x: x['value'], filter(lambda x: x['key']  == 'wp_clippinggd_fonte', p.custom_fields))
            aux_fonte = aux_fonte and aux_fonte[0] or ''

            aux_url_url   = map(lambda x: x['value'], filter(lambda x: x['key']  == 'wp_clippinggd_url', p.custom_fields))
            aux_url_anexo = map(lambda x: x['value'], filter(lambda x: x['key']  == 'wp_clippinggd_anexo' , p.custom_fields))

            if aux_url_anexo:
                aux_url = wordpress.getAttachmentUrl(postid = aux_url_anexo[0]) or ''
            else:
                aux_url = aux_url_url and aux_url_url[0] or ''

            url.append(aux_url)
            posttype.append(u'Clipping')
            txtdata.append('')
            excerpt.append('Fonte: '+aux_fonte)
            textobotao.append('Continue lendo')
            thumbs.append('')
        elif p.post_type == 'equipegd_equipe':
            title.append(p.title)
            aux_cargo = map(lambda x: x['value'], filter(lambda x: x['key']  == 'wp_equipegd_cargo', p.custom_fields))
            aux_cargo = aux_cargo and aux_cargo[0] or ''
            url.append('')
            posttype.append(u'Equipe')
            txtdata.append('')
            excerpt.append(aux_cargo)
            textobotao.append('')
            thumbs.append('')
        elif p.post_type == 'oquegd_oque':
            title.append(p.title)
            url.append('')
            posttype.append(u'Documentos')
            txtdata.append('')
            excerpt.append(p.content)
            textobotao.append('')
            thumbs.append('')
        elif p.post_type == 'post':
            title.append(p.title)
            aux_img = ''
            url.append('/post/'+p.slug)
            posttype.append(u'Notícias')
            txtdata.append(str(p.the_date.day)+' '+p.the_date.strftime("%B").capitalize()+' de '+str(p.the_date.year))
            excerpt.append(p.excerpt)
            textobotao.append('Continue lendo')
            if p.thumbs:
                if p.has_category('wide'):
                    aux_img = "<img src='"+str(p.thumbs['widenewsbox']['url'])+"' alt='"+unicode(p.title)+"' width='"+ str(p.thumbs['widenewsbox']['width']) +"' height='"+ str(p.thumbs['widenewsbox']['height']) +"' class='wide'>"
                elif p.thumbs:
                    aux_img = "<img src='"+str(p.thumbs['newsbox']['url'])+"'     alt='"+unicode(p.title)+"' width='"+ str(p.thumbs['newsbox']['width']) +"'     height='"+ str(p.thumbs['newsbox']['height']) +"'>"
            thumbs.append(aux_img or '')


    psearch = zip(title, url, posttype, txtdata, excerpt, textobotao, thumbs)

    return psearch

def formatarDataeHora(s,formato = '%d/%m/%Y %H:%Mh' ):
    z = str(s)
    z = z.replace("T", "")
    z = z.replace(":", "")
    z = datetime.datetime.strptime(z, "%Y%m%d%H%M%S")
    z = z.strftime(formato)
    return z

def formatarDataeHoraPostType(s,formato = '%b' ):
    z = str(s)
    z = datetime.datetime.strptime(z, "%Y-%m-%d %H:%M")
    z = z.strftime(formato)
    return z

app.jinja_env.filters['formatarDataeHora'] = formatarDataeHora
app.jinja_env.filters['formatarDataeHoraPostType'] = formatarDataeHoraPostType

@app.context_processor
def extend_context():
    """This function is a context processor. It injects variables such
    as `user' and `host' variable in all templates that will be rendered
    for this application"""

    context = {}

    # This will be used to bind socket.io client API to our
    # server. Without the port information.
    context['host'] = request.host.split(':')[0]

    # It's also useful to be able to access the configuration module
    # from some templates
    context['conf'] = conf

    # Time to add the `user' var
    try:
        context['user'] = authenticated_user()
    except NobodyHome:
        context['user'] = None

    # Job done!
    return context


@app.after_request
def cleanup(response):
    """Closes the database session that will be open once again in the
    next request"""
    dbsession.close()
    return response

@app.context_processor
def inject_thumborurl():
    def thumborurl(image, size):
        '''
        Método que cria, através da libthumbor
        a url codificada para exibição de imagens na galeria
        '''
        #print "CODIFICANDO:", size, image
        crypto = CryptoURL(key=app.config['THUMBOR_KEY'])
        codigo = crypto.generate(
            width=size[0] if isinstance(size[0], int) else None,
            height=size[1] if isinstance(size[1], int) else None,
            smart=True,
            image_url=image.replace('http://','')
        )
        #print "CODIGO:", codigo
        return app.config['THUMBOR_URL'] + codigo
    return dict(thumborurl=thumborurl)


# --- Static special pages ---
"""@app.route('/')
def index():
    return redirect('/audience')
"""

@app.route('/cachecleargd/')
def cachecleargd():
    global cache
    cache.cache.clear()
    return redirect(url_for('.index'))

@app.route('/')
@cache.cached(unless=is_authenticated)
def index():
    app.logger.error( " ######################################################################## BASE " )
    """Renders the index template"""
    menus = wordpress.exapi.getMenuItens(menu_slug='menu-principal')
    # slideshow = wordpress.getRecentPosts(
    #     category_name='highlights',
    #     post_status='publish',
    #     numberposts=4,
    #     thumbsizes=['slideshow'])
    #Retorna a ultima foto inserida neste album.
    # picday = wordpress.wpgd.getLastFromGallery(conf.GALLERIA_FOTO_DO_DIA_ID)
    # news = wordpress.getRecentPosts(
    #     category_name='news',
    #     post_status='publish',
    #     numberposts=6,
    #     thumbsizes=['newsbox', 'widenewsbox'])
    try:
        vote_url = app.config['VOTACAO_URL']
    except KeyError:
        vote_url = ""
    try:
        vote_root = app.config['VOTACAO_ROOT']
    except KeyError:
        vote_root = ""
    try:
        vote_altura = app.config['VOTACAO_ALTURA']
    except KeyError:
        vote_altura = ""

    try:
        twitter_hash_cabecalho = app.config['TWITTER_HASH_CABECALHO']
    except KeyError:
        twitter_hash_cabecalho = ""
    return render_template(
        'index.html', wp=wordpress,
        sidebar=wordpress.getSidebar,
        page_about=wordpress.getPageByPath('sobre'),
        page_pri=wordpress.getPageByPath('prioridades'),
        page_pq=wordpress.getPageByPath('por-que'),
        page_pro=wordpress.getPageByPath('processo'),
        page_como=wordpress.getPageByPath('como-funciona'),
        page_seg=wordpress.getPageByPath('seguranca-2'),
        menu=menus,
        VOTACAO_URL=vote_url,
        VOTACAO_ROOT=vote_root,
        VOTACAO_ALTURA=vote_altura,
        twitter_hash_cabecalho=twitter_hash_cabecalho
    )


@app.route('/getpart/<part>')
@cache.memoize(unless=is_authenticated)
def get_part(part):
    """Renders some layout parts used to build the "participate" menu"""
    return render_template('parts/%s.html' % part)

@app.route('/gallerias')
@cache.memoize(unless=is_authenticated)
def gallery():
    menus = wordpress.exapi.getMenuItens(menu_slug='menu-principal')
    try:
        twitter_hash_cabecalho = app.config['TWITTER_HASH_CABECALHO']
    except KeyError:
        twitter_hash_cabecalho = ""
    return render_template(
        'gallerys.html',
        twitter_hash_cabecalho=twitter_hash_cabecalho,
        menu=menus,
    )

@app.route('/teaser')
@cache.memoize(unless=is_authenticated)
def teaser():
    """Renders the teaser template"""
    return render_template('teaser.html')


@app.route('/sobre/')
@cache.memoize(unless=is_authenticated)
def sobre():
    """Renders the about template"""
    return render_template('sobre.html', page=wordpress.getPageByPath('sobre'),
        menu=wordpress.exapi.getMenuItens(menu_slug='menu-principal'))

@app.route('/about/')
@cache.memoize(unless=is_authenticated)
def about():
    """Renders the about template"""
    return render_template('about.html', page=wordpress.getPageByPath('about')
        ,menu=wordpress.exapi.getMenuItens(menu_slug='menu-principal'))

@app.route('/acerca/')
@cache.memoize(unless=is_authenticated)
def acerca():
    """Renders the about template"""
    return render_template('acerca.html', page=wordpress.getPageByPath('acerca')
        ,menu=wordpress.exapi.getMenuItens(menu_slug='menu-principal'))


@app.route('/foto_com_gov/')
@cache.memoize(unless=is_authenticated)
def foto_com_gov():
    return render_template('galeria.html')


# -- Blog specific views --


@app.route('/news/')
@app.route('/news/<int:page>/')
@cache.memoize(unless=is_authenticated)
def news(page=0):
    """List posts in chronological order"""
    menus = wordpress.exapi.getMenuItens(menu_slug='menu-principal')
    pagination, posts = wordpress.getPosts(page=page, thumbsizes=['newsbox', 'widenewsbox'])
    #Retorna a ultima foto inserida neste album.
    picday = wordpress.wpgd.getLastFromGallery(conf.GALLERIA_FOTO_DO_DIA_ID)

    psearch = _format_postsearch(posts)
    try:
        twitter_hash_cabecalho = app.config['TWITTER_HASH_CABECALHO']
    except KeyError:
        twitter_hash_cabecalho = ""

    return render_template(
        'archive.html',
        sidebar=wordpress.getSidebar,
        twitter_hash_cabecalho=twitter_hash_cabecalho,
        picday=picday,
        pagination=pagination,
        menu=menus,
        posts=psearch)


@app.route('/cat/<int:cid>/')
@app.route('/cat/<int:cid>/<int:page>/')
@cache.memoize(unless=is_authenticated)
def category(cid, page=0):
    """List posts of a given category"""
    pagination, posts = wordpress.getPostsByCategory(cat=cid, page=page)
    #Retorna a ultima foto inserida neste album.
    picday = wordpress.wpgd.getLastFromGallery(conf.GALLERIA_FOTO_DO_DIA_ID)

    psearch = _format_postsearch(posts)
    try:
        twitter_hash_cabecalho = app.config['TWITTER_HASH_CABECALHO']
    except KeyError:
        twitter_hash_cabecalho = ""
    return render_template(
        'archive.html',
        sidebar=wordpress.getSidebar,
        twitter_hash_cabecalho=twitter_hash_cabecalho,
        picday=picday,
        pagination=pagination,
        posts=psearch
        ,menu=wordpress.exapi.getMenuItens(menu_slug='menu-principal'))


@app.route('/tag/<string:slug>/')
@app.route('/tag/<string:slug>/<int:page>/')
@cache.memoize(unless=is_authenticated)
def tag(slug, page=0):
    """List posts of a given tag"""
    pagination, posts = wordpress.getPostsByTag(tag=slug, page=page)
    #Retorna a ultima foto inserida neste album.
    picday = wordpress.wpgd.getLastFromGallery(conf.GALLERIA_FOTO_DO_DIA_ID)

    psearch = _format_postsearch(posts)
    try:
        twitter_hash_cabecalho = app.config['TWITTER_HASH_CABECALHO']
    except KeyError:
        twitter_hash_cabecalho = ""
    return render_template(
        'archive.html',
        sidebar=wordpress.getSidebar,
        twitter_hash_cabecalho=twitter_hash_cabecalho,
        picday=picday,
        pagination=pagination,
        posts=psearch
        ,menu=wordpress.exapi.getMenuItens(menu_slug='menu-principal'))



@app.route('/conselho-comunicacao/')
@cache.memoize(unless=is_authenticated)
def conselho():
    """Renders a wordpress page special"""
    path = 'conselho-comunicacao'
    picday = wordpress.wpgd.getLastFromGallery(conf.GALLERIA_FOTO_DO_DIA_ID)
    page = wordpress.getPageByPath(path)
    cmts = wordpress.getComments(status='approve',post_id=page.data['id'], number=1000)
    try:
        twitter_hash_cabecalho = app.config['TWITTER_HASH_CABECALHO']
    except KeyError:
        twitter_hash_cabecalho = ""
    return render_template(
        'post.html',
        post=page,
        sidebar=wordpress.getSidebar,
        picday=picday,
        twitter_hash_cabecalho=twitter_hash_cabecalho,
        comments=cmts,
        show_comment_form=is_authenticated(),
        categoria_contribuicao_text=categoria_contribuicao_text
        ,menu=wordpress.exapi.getMenuItens(menu_slug='menu-principal')
    )


def add_filhos_and_comments_to_post(post_type, lista_de_posts):
    if type(lista_de_posts) in (tuple,list):
        for post in lista_de_posts:
            cmts = wordpress.getComments(status='approve',post_id=post['id'], number=1000)
            if cmts:
                post['_comments'] = cmts
            filhos = wordpress.getCustomPostByParent(post_type, post['id'] )
            if filhos:
                post['filhos'] = filhos
                add_filhos_and_comments_to_post(post_type, filhos)
    else:
        post = lista_de_posts
        cmts = wordpress.getComments(status='approve',post_id=post['id'], number=1000)
        if cmts:
            post['_comments'] = cmts
        filhos = wordpress.getCustomPostByParent(post_type, post['id'] )
        if filhos:
            post['filhos'] = filhos
            add_filhos_and_comments_to_post(post_type, filhos)


@app.route('/o-que-voce-espera-da-cultura-nos-proximos-10-anos/')
@cache.memoize(unless=is_authenticated)
def cultura():
    """Renders a wordpress page special"""
    path = 'artigo-especial-1'
    post_type = 'artigo-herarquico'
    # picday = wordpress.wpgd.getLastFromGallery(conf.GALLERIA_FOTO_DO_DIA_ID)
    post = wordpress.getCustomPostByPath(post_type,path)

    add_filhos_and_comments_to_post(post_type, post)

    print post
    try:
        twitter_hash_cabecalho = app.config['TWITTER_HASH_CABECALHO']
    except KeyError:
        twitter_hash_cabecalho = ""

    return render_template(
        'artigo_hierarquico.html',
        post=post,
        sidebar=wordpress.getSidebar,
        # picday=picday,
        twitter_hash_cabecalho=twitter_hash_cabecalho,
        show_comment_form=is_authenticated(),
        categoria_contribuicao_text=categoria_contribuicao_text
        ,menu=wordpress.exapi.getMenuItens(menu_slug='menu-principal')
    )


@app.route('/comite-transito/')
@cache.memoize(unless=is_authenticated)
def comite_transito():
    """Renders a wordpress page special"""
    try:
        twitter_hash_cabecalho = app.config['TWITTER_HASH_CABECALHO']
    except KeyError:
        twitter_hash_cabecalho = ""
    return render_template(
        'comite-transito.html',
        menu=wordpress.exapi.getMenuItens(menu_slug='menu-principal'),
        twitter_hash_cabecalho=twitter_hash_cabecalho,
        wp=wordpress,
        sidebar=wordpress.getSidebar,
    )


@app.route('/enviar-noticia/', methods=['POST',])
def salvar_noticia_comite():
    print "RECEBEU NOTICIA!!!"
    if request.method == 'POST':
        titulo = request.form['titulo']
        noticia = request.form['noticia']
        cn = ComiteNews()
        cn.title = unicode(titulo)
        cn.content = unicode(noticia)
        cn.user = authenticated_user()
        dbsession.commit()

        #Envia o email avisando que chegou uma nova contribuição
        sendmail(
            conf.COMITE_SUBJECT, conf.COMITE_TO_EMAIL,
            conf.COMITE_MSG % {
                'titulo': titulo,
                'noticia': noticia,
            }
        )
        return msg.ok(_(u'Thank you. Your contribution was successfuly sent.'))
    else:
        return msg.error(_(u'Method not allowed'))


@app.route('/cadastrar-comite/', methods=['POST',])
def cadastrar_comite():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        telefone = request.form['telefone']
        cidade = request.form['cidade']
        cn = CadastroComite()
        cn.nome = unicode(nome)
        cn.email = unicode(email)
        cn.telefone = unicode(telefone)
        cn.cidade = unicode(cidade)
        dbsession.commit()

        # #Envia o email avisando que chegou uma nova contribuição
        # sendmail(
        #     conf.COMITE_SUBJECT, conf.COMITE_TO_EMAIL,
        #     conf.COMITE_MSG % {
        #         'titulo': titulo,
        #         'noticia': noticia,
        #     }
        # )

        return msg.ok(_(u'Thank you. Your contribution was successfuly sent.'))
    else:
        return msg.error(_(u'Method not allowed'))


@app.route('/pages/<path:path>/')
@cache.memoize(unless=is_authenticated)
def pages(path):
    """Renders a wordpress page"""
    #Retorna a ultima foto inserida neste album.
    picday = wordpress.wpgd.getLastFromGallery(conf.GALLERIA_FOTO_DO_DIA_ID)
    try:
        twitter_hash_cabecalho = app.config['TWITTER_HASH_CABECALHO']
    except KeyError:
        twitter_hash_cabecalho = ""
    return render_template(
        'page.html',
        page=wordpress.getPageByPath(path),
        twitter_hash_cabecalho=twitter_hash_cabecalho,
        sidebar=wordpress.getSidebar,
        picday=picday
        ,menu=wordpress.exapi.getMenuItens(menu_slug='menu-principal')
    )

@app.route('/pages/<path:path>.json')
@cache.memoize(unless=is_authenticated)
def page_json(path):
    """Returns a page data in the JSON format"""
    page = wordpress.getPageByPath(path)
    return dumps(page and page.data or None)


@app.route('/post/<slug>/')
@cache.memoize(unless=is_authenticated)
def post_slug(slug):
    try:
        post = wordpress.getPostByPath(slug)
        if not post['id']:
            abort(404)
    except:
        abort(404)

    pid = post['id']

    if 'the_date' not in post.keys():
        # post['the_date'] = post['date']['date'].value
        post['the_date'] = datetime.datetime.strptime(post['date']['date'].value,'%Y%m%dT%H:%M:%S')

    """View that renders a post template"""
    recent_posts = wordpress.getRecentPosts(
        post_status='publish',
        numberposts=4)
    #Retorna a ultima foto inserida neste album.
    # picday = wordpress.wpgd.getLastFromGallery(conf.GALLERIA_FOTO_DO_DIA_ID)
    menus = wordpress.exapi.getMenuItens(menu_slug='menu-principal')
    try:
        twitter_hash_cabecalho = app.config['TWITTER_HASH_CABECALHO']
    except KeyError:
        twitter_hash_cabecalho = ""
    return render_template(
        'post.html',
        post=post,
        tags=wordpress.getTagCloud(),
        sidebar=wordpress.getSidebar,
        # picday=picday,
        twitter_hash_cabecalho='#gov',
        menu=menus,
        comments=wordpress.getComments(status='approve',post_id=pid),
        show_comment_form=is_authenticated(),
        recent_posts=recent_posts)


@app.route('/post/<int:pid>/')
@cache.memoize(unless=is_authenticated)
def post(pid):
    try:
        p = wordpress.getPost(pid)
    except:
        return abort(404)
    """View that renders a post template"""
    recent_posts = wordpress.getRecentPosts(
        post_status='publish',
        numberposts=4)
    #Retorna a ultima foto inserida neste album.
    # picday = wordpress.wpgd.getLastFromGallery(conf.GALLERIA_FOTO_DO_DIA_ID)
    menus = wordpress.exapi.getMenuItens(menu_slug='menu-principal')

    try:
        twitter_hash_cabecalho = app.config['TWITTER_HASH_CABECALHO']
    except KeyError:
        twitter_hash_cabecalho = ""
    return render_template(
        'post.html',
        post=p,
        tags=wordpress.getTagCloud(),
        sidebar=wordpress.getSidebar,
        # picday=picday,
        twitter_hash_cabecalho=twitter_hash_cabecalho,
        menu=menus,
        comments=wordpress.getComments(status='approve',post_id=pid),
        show_comment_form=is_authenticated(),
        recent_posts=recent_posts)
    return post_page(pid)

@app.route('/new_contribution', methods=('POST',))
def new_contribution():
    """Posts new contributions on the page 'conselho-comunicacao' """

    try:
        mostrar_nome = request.form['mostrar_nome']
    except KeyError :
        mostrar_nome = 'N'

    if not is_authenticated():
        return msg.error(_(u'User not authenticated'))
    try:
        print "\n\nMOSTRAR NOME!", mostrar_nome
        cid = wordpress.newComment(
            username=session['username'],
            password=session['password'],
            post_id=request.form['post_id'],
            content=request.form['content1'] or request.form['content2'],
            categoria_sugestao=request.form['categoria_sugestao'],
            mostrar_nome=mostrar_nome
        )
        return msg.ok(_(u'Thank you. Your contribution was successfuly sent.'))
    except xmlrpclib.Fault, err:
        return msg.error(_(err.faultString), code='CommentError')

@app.route('/new_comment/', methods=('POST',))
def new_comment():
    """Posts new comments to the blog"""
    if not is_authenticated():
        return msg.error(_(u'User not authenticated'))
    try:
        wordpress.newComment(
            username=session['username'],
            password=session['password'],
            post_id=request.form['post_id'],
            content=request.form['content']
        )
        return msg.ok(_(u'Thank you. Your comment was successfuly sent'))
    except xmlrpclib.Fault, err:
        return msg.error(_(err.faultString), code='CommentError')


@app.route('/search/')
@app.route('/search/<int:page>/')
def search(page=0):
    """Renders the search template"""

    query = request.values.get('s', '') or request.values.get('buscatop', '')
    #posttype = ['audiencia_govesc', 'clippinggd_clipping', 'equipegd_equipe', 'oquegd_oque', 'post']
    pagination, posts = wordpress.search(s=query, page=page, thumbsizes=['newsbox', 'widenewsbox'])
    #Retorna a ultima foto inserida neste album.
    picday = wordpress.wpgd.getLastFromGallery(conf.GALLERIA_FOTO_DO_DIA_ID)

    psearch = _format_postsearch(posts)
    try:
        twitter_hash_cabecalho = app.config['TWITTER_HASH_CABECALHO']
    except KeyError:
        twitter_hash_cabecalho = ""

    return render_template(
        'archive.html',
        sidebar=wordpress.getSidebar,
        picday=picday,
        pagination=pagination,
        twitter_hash_cabecalho=twitter_hash_cabecalho,
        search_term=query,
        posts=psearch,
        menu=wordpress.exapi.getMenuItens(menu_slug='menu-principal'))


@app.route('/feed/')
def feed():
    """Renders the RSS wordpress function"""
    header = {'Content-Type': 'application/rss+xml; charset=utf-8'}
    return wordpress.getRSS(), 200, header

@app.route('/archive/<int:m>/')
@app.route('/archive/<int:m>/<int:page>/')
def archive(m, page=0):
    """List posts of the archive given yyyymm format"""
    pagination, posts = wordpress.getArchivePosts(m=m, page=page)
    #Retorna a ultima foto inserida neste album.
    picday = wordpress.wpgd.getLastFromGallery(conf.GALLERIA_FOTO_DO_DIA_ID)

    psearch = _format_postsearch(posts)
    try:
        twitter_hash_cabecalho = app.config['TWITTER_HASH_CABECALHO']
    except KeyError:
        twitter_hash_cabecalho = ""
    return render_template(
        'archive.html',
        sidebar=wordpress.getSidebar,
        picday=picday,
        twitter_hash_cabecalho=twitter_hash_cabecalho,
        pagination=pagination,
        posts=psearch)


@app.route('/confirm_signup/<string:key>/')
def confirm_signup(key):
    try:
        user = User.query.filter_by(user_activation_key=key).one()
        user.user_activation_key = ''
        dbsession.commit()
    except NoResultFound:
        return redirect(url_for('.index'))
    return redirect('%s?concluido' % url_for('.index'))
