# edit config file

exec {'echo':
  command => "PasswordAuthentication no \nIdentifyFile ~/.ssh/school" >> /etc/ssh/ssh_config,
  path    => '/bin'
}
