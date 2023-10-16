# fixes the system file descriptor limit for nginx
exec { 'file_desciptor_fix' :
  command => 'sudo sed -i \'s/15/4096/g\' /etc/default/nginx; sudo service nginx restart',
  path    => '/usr/bin/:/bin/',
}
