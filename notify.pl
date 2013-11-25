sub escape {
  my ($text) = @_;
  $text =~ s/"/\\"/g;
  $text =~ s/\$/\\\$/g;
  $text =~ s/`/\\"/g;
  return $text;
}

sub notify_private {
  my ($server, $msg, $nick, $addr) = @_;
  $msg = escape($msg);
  $nick = escape($nick);
  system("wget -qO- \"localhost:9871/notify?info= - Nouveau message privé de $nick - \n$msg\" &> /dev/null");
}

sub notify_public {
  my ($server, $msg, $nick, $addr, $target) = @_;
  $msg = escape($msg);
  $nick = escape($nick);
  system("wget -qO- \"localhost:9871/notify?info= - Nouveau message de $nick - \n$msg\" &> /dev/null");
}

Irssi::signal_add("message private", "notify_private");
Irssi::signal_add("message public", "notify_public")
