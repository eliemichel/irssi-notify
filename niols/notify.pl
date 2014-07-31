use URI::Escape;

my $port = 8005;
my $endpoint = "http://localhost:$port/notify";

sub notify {
    my %args = @_;

    my $post_data = '';
    while (($key, $val) = each(%args)) {
        if ($post_data ne '') {
            $post_data .= '&';
        }
        $post_data .= $key . '=' . uri_escape($val);
    }

    system(
        'wget',
        '--post-data='.$post_data,
        '-o', '/dev/null',
        '-O', '/dev/null',
        '-t', '1',
        '-T', '5',
        $endpoint,
        );
}


sub notify_private {
    my ($server, $msg, $nick, $addr) = @_;
    notify(
        msg => $msg,
        nick => $nick,
        chan => ''
        );
}

sub notify_public {
    my ($server, $msg, $nick, $addr, $target) = @_;
    notify(
        msg => $msg,
        nick => $nick,
        chan => $target
        );
}

Irssi::signal_add('message private', 'notify_private');
Irssi::signal_add('message public', 'notify_public');
