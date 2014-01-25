Introduction
============

DataTables_ is a plug-in for the jQuery_ Javascript library.
It is a highly flexible tool, based upon the principle of progressive
enhancement, which will add advanced interaction controls to any HTML table.

This version includes datatables 1.9.4 without the examples available in the
source distribution of the plugin. It is provided with an
``@@example.datatables`` view (not activated by default).

Install
=======

A genericsetup profile is provided to add ``jquery.dataTables`` to
``portal_javascript`` in a minified version with compression option set
to *none*.

Key features of jquery.dataTables
=================================

* Variable-length pagination
* On-the-fly filtering
* Multi-column sorting with data type detection
* Smart handling of column widths
* Display data from almost any data source
* Scrolling options for table viewport
* Fully internationalisable
* jQueryUI ThemeRoller support
* Rock solid - backed by a suite of 1400+ unit tests
* Wide variety of plug-ins inc. TableTools, FixedHeader and KeyTable
* It's free!
* State saving
* Hidden columns
* Dynamic creation of tables
* Ajax auto-loading of data
* Custom DOM positioning
* Single-column filtering
* Alternative pagination types
* Non-destructive DOM interaction
* Sorting column(s) highlighting
* Extensive plug-in support
* Fully themeable by CSS
* Solid documentation
* 60+ pre-built examples
* Full support for Adobe AIR
* Source available at github_

Plugins
=======

This addon embed extras plugins:

* AutoFill     1.1.2
* ColReorder   1.0.5
* ColVis       1.0.7
* FixedColumns 2.0.3
* FixedHeader  2.0.6
* KeyTable     1.1.7
* Scroller     1.0.1
* TableTools   2.0.3

How to use tabletools
---------------------
First include dependencies in your template, or register theses in
portal_javascripts::

  <link rel="stylesheet" type="text/css" media="screen" href="++resource++jquery.datatables/media/css/jquery.dataTables.css">
  <link rel="stylesheet" type="text/css" media="screen" href="++resource++jquery.datatables/extras/TableTools/media/css/TableTools.css">
  <script type="text/javascript" src="++resource++jquery.datatables.js"></script>
  <script type="text/javascript" src="++resource++jquery.datatables/extras/TableTools/media/js/ZeroClipboard.js"></script>
  <script type="text/javascript" src="++resource++jquery.datatables/extras/TableTools/media/js/TableTools.js"></script>
  <style type="text/css">.clear{clear:both}</style>


Next you can create your datatable::

  var oTable = $('#mydatatable').dataTable({
    "sDom": 'T<"clear">lfrtip',
    "oTableTools": {"sSwfPath": "++resource++jquery.datatables/extras/TableTools/media/swf/copy_csv_xls_pdf.swf"}
  });

How to use translations
-----------------------

This addon provide translations of datatables. To use translations you have
to init your datatables providing sUrl param::

  $(document).ready(function() {
    $('#example').dataTable( {
        "oLanguage": {
            "sUrl": "@@collective.js.datatables.translation"
        }
    } );
  } );


Credits
=======

Companies
---------

|makinacom|_

* `Planet Makina Corpus <http://www.makina-corpus.org>`_
* `Contact us <mailto:python@makina-corpus.org>`_

Authors
-------

- JeanMichel FRANCOIS aka toutpt <toutpt@gmail.com>

Contributors
------------

- Nejc Zupan (zupo)
- Martijn Pieters
- Luca Fabbri (keul)
- Jens Klein (jensens)

.. |makinacom| image:: http://depot.makina-corpus.org/public/logo.gif
.. _makinacom:  http://www.makina-corpus.com
.. _DataTables: http://www.datatables.net/download
.. _github: https://github.com/DataTables
.. _jQuery: http://jquery.com

