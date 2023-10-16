# fixes file descriptor limit for user holberton
exec { 'fix':
  command => "sed -i 's/nofile [0-9]/nofile 50000/g' /etc/security/limits.conf",
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
}
