# Create a file named school in /tmp

file {'/tmp/school':
  content => 'I love puppet',
  group   => 'www-data',
  mode    => '0744',
  owner   => 'www-data',
}
