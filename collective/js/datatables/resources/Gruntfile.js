/* global module */

module.exports = function(grunt) {
  'use strict';

  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),
    requirejs: {
      compile: {
        options: {
          baseUrl: './',
          name: 'node_modules/datatables/media/js/jquery.dataTables.min.js',
          out: 'media/js/jquery.dataTables.min.js',
          stubModules: ['jquery'],
          optimize: 'none',
          paths: {
            'jquery': 'empty:'
          }
        }
      }
    }
  });

  grunt.loadNpmTasks('grunt-contrib-copy');
  grunt.loadNpmTasks('grunt-contrib-clean');
  grunt.loadNpmTasks('grunt-contrib-requirejs');

  grunt.registerTask('prod', [
    'requirejs:compile'
  ]);
};
