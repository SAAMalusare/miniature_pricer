#!c:/Perl/bin/perl.exe
	use	strict;
	use warnings;
	use CGI;
	use db_class;
	
	my 	$obj_db  = db_class->new();
	my 	($server)= $obj_db->http_server();
	my 	$obj_cgi = CGI->new();
	
	print $obj_cgi->header();
	print $obj_cgi->start_html (
	                        		-title=> 'Minature Pricing System',
	                        		-style=>{'src'=>"/minature/images/style.css"},
	                        	);
	
	print $obj_cgi->start_form(
	                        -name=>'Minature_Pricinge',
	                        -method=>'Post',
	                        -action=>"http://$server/cgi-bin/minature/miniture.cgi",
	                    );

	my 	($time)		 =($obj_cgi->param('time')); chomp $time;
	my 	($intrest)	 = $obj_db->get_rates($time); 
	my 	 $curr_price = 50;
		
	print '<div align="center">';			
	print 	$obj_cgi->br;
	print 	$obj_cgi->start_table({-border=>"0", -width=>'50%',-cellspacing=>0, -cellpadding=>0});
	print 	$obj_cgi->center
			(
				$obj_cgi->Tr({-style=>'font-size : 18px; color: white;', -align=>'center', -bgcolor=>'#3090C7'},
							   $obj_cgi->td({-colspan=>4},'Minature Pricing Server'),
							 ),
				$obj_cgi->Tr({-style=>'font-size : 18px; color: white;', -align=>'left', -bgcolor=>'#8FBAC8'},
							   $obj_cgi->td('Current Spot Price ($)'),
							   $obj_cgi->td($obj_cgi->textfield( -name=>'price', 
	  								  							 -size=>25, 
	  								   							 -value=>"$curr_price")
	  								   		),
							 ),
				$obj_cgi->Tr({-style=>'font-size : 18px; color: white;', -align=>'left', -bgcolor=>'#8FBAC8'},
							   $obj_cgi->td('Time [in days]'),
							   $obj_cgi->td($obj_cgi->textfield( -name=>'time', 
	  								  							 -size=>25, 
	  								  							 -override=>0,
	  								   							 -maxlength=>6,)
	  								   		),
							 ),	
				$obj_cgi->Tr({-style=>'font-size : 18px; color: white;', -align=>'left', -bgcolor=>'#8FBAC8'},
							   $obj_cgi->td('Annual Intrest Rate'),
							   $obj_cgi->td($obj_cgi->textfield( -name=>'int', 
	  								  							 -size=>25, 
	  								   							 -value=>"$intrest \%",
									   				  			 -override=>1,
									   				  			 -size=>25,
									   				  			 -disabled 
	  								   							 )
	  								   		),
							 ),	
			);

	if 	($time and $intrest and $curr_price)
		{
			my ($future_con) = $obj_db->get_future_contract($time, $intrest, $curr_price);
			if ($future_con)
				{
					print $obj_cgi->center
							(
								$obj_cgi->Tr({-style=>'font-size : 18px; color: white;', -align=>'left', -bgcolor=>'#8FBAC8'},
										      $obj_cgi->td('Future Contract ($)'),
										      $obj_cgi->td($obj_cgi->textfield(-name=>'Future_Contract',-value=>"$future_con", -size=>25,-override=>1)),
										    ),
							);
				}	
		}
	
	print $obj_cgi->center
			(
				$obj_cgi->Tr({-align=>'center', -bgcolor=>'#3090C7'},
								$obj_cgi->td($obj_cgi->submit( 
								   								  -style=>'font-size : 15px;', 
								   								  -align=>'center', 
								   								  -bgcolor=>'#D2B9D3', 
								   								  -name=>'Submit', 
					  				  						 )
					  				   		),
					  			$obj_cgi->td($obj_cgi->reset(-style=>'font-size : 15px; color:', -align=>'left', -bgcolor=>'#D2B9D3',
					  										  -onClick=>"window.location.href='http://$server/cgi-bin/minature/miniture.cgi';return false", 
					  										  -width=>455,	
					  										)
					  				   		),
					  		),			 			 		 			 
			);
		
	print 	$obj_cgi->end_table();
	print '</div>';			
	print 	$obj_cgi->end_html;