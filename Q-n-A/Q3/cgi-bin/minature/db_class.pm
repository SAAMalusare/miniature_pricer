package db_class;

	use strict;
	use warnings;
	use DBI;
	use DBD::ODBC;
	
	sub new
		{
			my $self = {};
			return bless $self;
		} 
		
	sub databaseconnection
		{
			my $self = shift;
			my ($str_server, $str_db, $str_user, $str_pwd, $Fms_Path);
			
			open (DB, 'Dbconnection.xml');
			my @ar_filebuf = <DB>;
			close DB;
			my $str_joined_buf = join "", @ar_filebuf;
			$str_joined_buf =~s/\s+//g;
			
			$str_joined_buf =~s{<DataBaseLive><Server>(.+?)</Server><Name>(.+?)</Name><User>(.+?)</User><Pwd>(.+?)</Pwd></DataBaseLive>}
									   {
									   		($str_server, $str_db, $str_user, $str_pwd) = ($1,$2,$3,$4);
									   }exgsi;
		
			my $str_DSN = "DBI:mysql:database=$str_db;host=$str_server;port=3306, { AutoCommit => 0}";
			my $str_dbh = DBI->connect($str_DSN, $str_user, $str_pwd) or warn "$DBI::errstr\n";
			
			@ar_filebuf =();
			$str_joined_buf=undef;
			
			return ($str_dbh);
		}		

	sub http_server
		{
			my $self = shift;
			my ($str_server);
			
			open (DB, 'Dbconnection.xml');
			my @ar_filebuf = <DB>;
			close DB;
			my $str_joined_buf = join "", @ar_filebuf;
			$str_joined_buf =~s/\s+//g;
			
			$str_joined_buf =~s{<Http_Server>(.+?)</Http_Server>}
									   {
									   		$str_server = $1;
									   }exgsi;
			@ar_filebuf =();
			$str_joined_buf=undef;
												   
			return $str_server;
		}
		
	sub get_rates
		{
			my 	$self=shift;
			my 	$str_dbh = $self->databaseconnection();
			my 	($days) = (@_);
			my 	$sth = $str_dbh->prepare(qq{SELECT clm_rate FROM tbl_rate where clm_days <= $days order by clm_days desc limit 1;})or die $str_dbh->errstr;
				$sth->execute;
			while (my $ref = $sth->fetchrow_hashref()) 
						{
							return	$ref->{'clm_rate'};
						}		
		}

	sub	get_future_contract
		{
			my 	$self=shift;
			my 	($time, $intrest, $curr_price)=(@_);
			return  ($curr_price * (2.718 ** (($intrest/100) * ($time/365)))); 
		}

1;		