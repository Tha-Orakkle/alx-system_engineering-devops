# Installs and configures Nginx web server with Puppet
include stdlib

$new_page="https://www.youtube.com/watch?v=EJC-_j3SnXk"
$red_line="\trewrite ^/redirect_me/$ ${new_page} permanent;"

exec { 'update packages':
	provider => shell,
	command  => 'sudo apt-get update'
}

package { 'nginx':
	ensure  => 'installed',
	require => Exec['update packages']
}

exec { 'restart nginx':
	provider => shell,
	command  => 'sudo service nginx restart',
	require  => Package['nginx']
}

file { '/var/www/html/index.html':
	ensure  => 'present',
	content => 'Hello World!',
	mode    => '0644',
	owner   => 'root',
	group   => 'root'
}

file_line { 'set 301 redirection':
	ensure   => 'present',
	after    => 'server_name _;',
	path     => '/etc/nginx/sites-available/default',
	multiple => 'false',
	line     => $red_line,
	notify   => Exec['restart nginx'],
	require  => File['/var/www/html/index.html']
}
