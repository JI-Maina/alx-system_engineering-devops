#!/usr/bin/env ruby
puts ARGV[0].scan(/from:(.\w+)/).scan(/to:([+\w+]+)/).scan(/flags:(.{12})/).join(',')
