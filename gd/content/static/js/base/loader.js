/* Copyright (C) 2012  Sérgio Berlotto <sergio.berlotto@gmail.com>
 * Copyright (C) 2012  Governo do Estado do Rio Grande do Sul
 *
 *   Author: Guilherme Guerra <guerrinha@comum.org>
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU Affero General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU Affero General Public License for more details.
 *
 * You should have received a copy of the GNU Affero General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */

$(document).ready(function() {
	
	console.log("Adicionado método para show loading novo...");

	jQuery.fn.showLoadingModal = function() {
	    // $("#content-loading").addClass("newloading"); 
	    $("#content-loading").show(); 
	};

	jQuery.fn.hideLoadingModal = function() {
	    // $("#content-loading").removeClass("newloading"); 
	    $("#content-loading").hide(); 
	};

});
