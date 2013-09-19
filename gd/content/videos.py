
# -*- coding:utf-8 -*-
#
# Copyright (C) 2011  Governo do Estado do Rio Grande do Sul
#
#   Author: Lincoln de Sousa <lincoln@gg.rs.gov.br>
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

from flask import Blueprint, render_template, current_app, request, redirect
from gd.utils.gdcache import fromcache, tocache, removecache
from gd.utils import twitts
#from gd.auth import is_authenticated
from gd.content.wp import wordpress

videos = Blueprint(
    'videos', __name__,
    template_folder='templates',
    static_folder='static')

@videos.route('/')
def redir_videos_recentes():
    return redirect("/videos/recentes")


@videos.route('/recentes')
@videos.route('/populares')
def listing():

    # hvideos = wordpress.wpgd.getHighlightedVideos()
    hvideos = fromcache("h_videos_root") or tocache("h_videos_root",
        wordpress.wpgd.getHighlightedVideos() )

    print "========================================================"
    # print dir(request)
    # print request.url
    print request.url_rule
    print "========================================================"

    if 'populares' in str(request.url_rule):
        order = "views" #recents
        nome_canal = "Populares"
    else :
        order = "date"
        nome_canal = "Recentes"

    order_by = "%s desc" % order

    videos_json = {}
    allvideos = fromcache("all_videos_root_") or tocache("all_videos_root_" ,wordpress.wpgd.getVideos(
        where='status=true', orderby="date DESC" ))

    categories = fromcache("all_videos_categories") or tocache("all_videos_categories",wordpress.wpgd.getVideosCategories())

    for v in allvideos:
        videos_json[v['title']] = v['id']

    print "Buscando", current_app.config['VIDEO_PAGINACAO'], "vídeos por página!"
    videos = fromcache("videos_root_%s" % order) or tocache("videos_root_%s" % order,
        wordpress.wpgd.getVideos(where='status=true', orderby=order_by, limit=current_app.config['VIDEO_PAGINACAO']) )

    try:
        twitter_hash_cabecalho = twitts()
    except KeyError:
        twitter_hash_cabecalho = ""

    menus = fromcache('menuprincipal') or tocache('menuprincipal', wordpress.exapi.getMenuItens(menu_slug='menu-principal') )
    return render_template('videos.html', videos=videos
        ,twitter_hash_cabecalho=twitter_hash_cabecalho
        ,menu=menus, titulos=videos_json, categories=categories, hvideos=hvideos
        ,canal=nome_canal)

@videos.route('/canal/<int:categoria_id>')
def canal(categoria_id):
    categories = fromcache("all_videos_categories") or tocache("all_videos_categories",wordpress.wpgd.getVideosCategories())

    print categories
    nome_canal = ""
    for cat in categories:
        if int(cat['term_id']) == categoria_id:
            nome_canal = cat['name']
            break

    videos = fromcache("videos_canal_%s" % str(categoria_id)) or tocache("videos_canal_%s" % str(categoria_id),
             wordpress.wpgd.getVideosByCategory(category=categoria_id, orderby='date DESC'))

    videos_json = {}
    allvideos = fromcache("all_videos_root") or tocache("all_videos_root",wordpress.wpgd.getVideos(
        where='status=true', orderby='title'))
    for v in allvideos:
        videos_json[v['title']] = v['id']

    hvideos = fromcache("h_videos_root") or tocache("h_videos_root",
        wordpress.wpgd.getHighlightedVideos() )

    return render_template('videos.html', videos=videos, titulos=videos_json,
        categories=categories, hvideos=hvideos, canal=nome_canal)


@videos.route('/nextpage/<int:pagina>/')
def nextpage(pagina):
    paginacao = int(current_app.config['VIDEO_PAGINACAO'])
    offset = pagina * paginacao
    print "OFFSET:", offset
    videos = fromcache("videos_%s" % str(offset)) or tocache("videos_%s" % str(offset), wordpress.wpgd.getVideos(
        where='status=true', orderby='date DESC', limit=paginacao,
        offset=offset))
    return render_template('videos_pagina.html', videos=videos)


@videos.route('/<int:vid>/')
def details(vid):
    video = fromcache("video_%s" % str(vid))
    print "Video do cache!"

    if not video:
        print "Video do wordpress..."
        video = tocache("video_%s" % str(vid), wordpress.wpgd.getVideo(vid))

    video['views'] = int(video['views']) + 1
    # print "Delete video cache!"
    removecache("video_%s" % str(vid))
    # print "Set video to cache!"
    tocache("video_%s" % str(vid), video)
    wordpress.wpgd.setVideoViews(video['views'], vid);

    sources = fromcache("video_src_%s" % str(vid)) or tocache("video_src_%s" % str(vid),wordpress.wpgd.getVideoSources(vid))

    base_url = current_app.config['BASE_URL']
    base_url = base_url if base_url[-1:] != '/' else base_url[:-1] #corta a barra final
    video_sources = {}
    for s in sources:
        if(s['format'].find(';') > 0):
            f = s['format'][0:s['format'].find(';')]
        else:
            f = s['format']
        video_sources[f] = s['url']
    try:
        twitter_hash_cabecalho = twitts()
    except KeyError:
        twitter_hash_cabecalho = ""

    menus = fromcache('menuprincipal') or tocache('menuprincipal', wordpress.exapi.getMenuItens(menu_slug='menu-principal') )
    return render_template('video.html', video=video, sources=video_sources
        ,menu=menus
        ,twitter_hash_cabecalho=twitter_hash_cabecalho
        ,base_url=base_url)


@videos.route('/embed/<int:vid>/')
def embed(vid):
    video = fromcache("video_%s" % str(vid)) or tocache("video_%s" % str(vid), wordpress.wpgd.getVideo(vid))
    sources = fromcache("video_src_%s" % str(vid)) or tocache("video_src_%s" % str(vid),wordpress.wpgd.getVideoSources(vid))
    video_sources = {}
    for s in sources:
        if(s['format'].find(';') > 0):
            f = s['format'][0:s['format'].find(';')]
        else:
            f = s['format']
        video_sources[f] = s['url']
    return render_template('videoembed.html', video=video, sources=video_sources)
