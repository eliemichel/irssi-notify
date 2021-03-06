use URI::Escape;

my $port = 9871;
my $endpoint = "http://localhost:$port/notify";

sub send_request {
  my %args = @_;

  my $post_data = "";

  while (($key, $val) = each(%args)) {
    if ($post_data ne "") {
      $post_data .= "&";
    }
    $post_data .= $key . "=" . uri_escape($val);
  }

  system(
      "wget",
      "--post-data=" . $post_data,
      "-o", "/dev/null",
      "-O", "/dev/null",
	  "-T", "5",
      $endpoint
    );
}


sub notify_private {
  my ($server, $msg, $nick, $addr) = @_;

  send_request(
        "nick" => $nick,
        "msg" => $msg,
        "chan" => "",
  );
}

sub notify_public {
  my ($server, $msg, $nick, $addr, $target) = @_;

  send_request(
      "nick" => $nick,
      "msg" => $msg,
      "chan" => $target,
  );
}

Irssi::signal_add("message private", "notify_private");
Irssi::signal_add("message public", "notify_public")
