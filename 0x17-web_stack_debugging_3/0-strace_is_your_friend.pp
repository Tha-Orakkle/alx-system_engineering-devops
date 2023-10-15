# fixes incorrect file extension in the wp-settings.php file
exec { 'fix_extension':
  command => 'sed -i \'s/class-wp-locale.phpp/class-wp-locale.php/\' /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'
}
