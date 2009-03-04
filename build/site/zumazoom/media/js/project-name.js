/**
 * $Id: [project-name].js yyyy-mm-dd $
 *
 * @author [Developer Name]
 * @copyright Copyright (c) 2008, Trapeze, All rights reserved.
 *
 * Requirements:
 *      jQuery 1.2.6 (http://www.jquery.com),
 */


if (typeof trapeze == "undefined") var trapeze = new Object();

trapeze.[project_name] = {	
	//Preload Function
    preload_images : function() {
        var a = (typeof arguments[0] == 'object')? arguments[0] : arguments;
        for(var i = a.length -1; i > 0; i--) {
            $("<img />").attr("src", a[i]);
        }
    },

    // Place your functions here

	init : function() {
        var page = $('body').attr('class');
        page = (page.indexOf(' ') > 0) ? page.slice(0,page.indexOf(' ')) : page;
        switch(page) {
            case 'home-page':
                //Code to be executed on the home page
                break;
            case 'about-page':
                //Code to be executed on the about page
                break;
            default:
                //Code to be executed on any page, but the pages listed above.
        }

        // Code to be executed on every page
	}
};

$(function() {
   // Code to execute when the DOM is ready
	trapeze.[project_name].init();
});