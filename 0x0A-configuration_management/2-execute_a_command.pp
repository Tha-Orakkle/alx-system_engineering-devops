# kills a process named 'killmenow'

exec { 'pkill':
  path => '/usr/bin/:/usr/local/bin/:/bin/'
}
