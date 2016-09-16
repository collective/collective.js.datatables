Development/Updates
===================

DataTables has it's very own way of packaging it's resources and doesn't play well with require.js as we use it.

To use DataTables with Plone you have to add these undefine/define snippets before and after the orignal minified version of the distribution.

Snippet
-------

::
    old_define = define;
    define = undefined;
    old_require = require;
    require = undefined;

    [jquery.dataTables.min.js]

    define = old_define;
    require = old_require;
