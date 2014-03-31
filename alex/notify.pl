use LWP::UserAgent;
use HTTP::Request::Common;

my $ua = LWP::UserAgent->new;

my $port = 9876;
my $endpoint = "http://127.0.0.1:$port/notify";


sub notify_private {
  my ($server, $msg, $nick, $addr) = @_;

  $ua->request(
	  POST $endpoint,
	  Content => [
		nick => $nick,
		msg => $msg,
		chan => "",
	  ],
  );
}

sub notify_public {
  my ($server, $msg, $nick, $addr, $target) = @_;

  $ua->request(
	  POST $endpoint,
	  Content => [
		nick => $nick,
		msg => $msg,
		chan => $target,
	  ],
  );
}

Irssi::signal_add("message private", "notify_private");
Irssi::signal_add("message public", "notify_public")
