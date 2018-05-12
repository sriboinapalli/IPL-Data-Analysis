import pandas as pd
import numpy as np
import matplotlib.pyplot as ply

pd.set_option('display.width',120)

#2017

dd_b_b_f = pd.read_html("http://stats.espncricinfo.com/indian-premier-league-2017/engine/records/averages/batting_bowling_by_team.html?id=11701;team=4344;type=tournament", index_col = 0)
delhi_batting_2017 = dd_b_b_f[0]
delhi_batting_2017["Team"] = "DD"
country = np.array(["IND","IND","RSA","IND","IND","ENG","IND","NZ","RSA","SL","AUS","IND","WI","IND","WI","IND","IND","IND","IND"])
delhi_batting_2017["Country"] = pd.Series(country, delhi_batting_2017.index)
big_data_2017 = delhi_batting_2017

gl_b_b_f = pd.read_html("http://stats.espncricinfo.com/indian-premier-league-2017/engine/records/averages/batting_bowling_by_team.html?id=11701;team=5845;type=tournament", index_col = 0)
gujarat_batting_2017 = gl_b_b_f[0]
gujarat_batting_2017["Team"] = "GL"
gl_country_2017 = np.array(["IND","IND","IND","ENG","NZ","IND","AUS","AUS","WI","AUS","IND","IND","IND","IND","IND","IND","IND","IND","IND","IND","IND","IND","IND","IND"])
gujarat_batting_2017["Country"] = pd.Series(gl_country_2017, gujarat_batting_2017.index)
big_data_2017 = big_data_2017.append(gujarat_batting_2017)

kxip_b_b_f = pd.read_html("http://stats.espncricinfo.com/indian-premier-league-2017/engine/records/averages/batting_bowling_by_team.html?id=11701;team=4342;type=tournament", index_col = 0)
kxip_batting_2017 = kxip_b_b_f[0]
kxip_batting_2017["Team"] = "KXIP"
kxip_country_2017 = np.array(["RSA","AUS","AUS","IND","RSA","IND","IND","NZ","IND","ENG","IND","IND","IND","AUS","IND","IND","IND","IND","IND","NZ","IND"])
kxip_batting_2017["Country"] = pd.Series(kxip_country_2017, kxip_batting_2017.index)
big_data_2017 = big_data_2017.append(kxip_batting_2017)

kkr_b_b_f = pd.read_html("http://stats.espncricinfo.com/indian-premier-league-2017/engine/records/averages/batting_bowling_by_team.html?id=11701;team=4341;type=tournament", index_col = 0)
kkr_batting_2017 = kkr_b_b_f[0]
kkr_batting_2017["Team"] = "KKR"
kkr_country_2017 = np.array(["IND","AUS","IND","IND","IND","IND","IND","IND","WI","NZ","ENG","IND","AUS","IND","IND","IND","WI","NZ","BD"])
kkr_batting_2017["Country"] = pd.Series(kkr_country_2017, kkr_batting_2017.index)
big_data_2017 = big_data_2017.append(kkr_batting_2017)

mi_b_b_f = pd.read_html("http://stats.espncricinfo.com/indian-premier-league-2017/engine/records/averages/batting_bowling_by_team.html?id=11701;team=4346;type=tournament", index_col = 0)
mi_batting_2017 = mi_b_b_f[0]
mi_batting_2017["Team"] = "MI"
mi_country_2017 = np.array(["IND","IND","IND","IND","WI","ENG","IND","IND","WI","IND","IND","IND","IND","NZ","NZ","AUS","SL","IND"])
mi_batting_2017["Country"] = pd.Series(mi_country_2017, mi_batting_2017.index)
big_data_2017 = big_data_2017.append(mi_batting_2017)

rps_b_b_f = pd.read_html("http://stats.espncricinfo.com/indian-premier-league-2017/engine/records/averages/batting_bowling_by_team.html?id=11701;team=5843;type=tournament", index_col = 0)
rps_batting_2017 = rps_b_b_f[0]
rps_batting_2017["Team"] = "RPS"
rps_country_2017 = np.array(["AUS","IND","ENG","IND","IND","IND","IND","IND","AUS","IND","IND","IND","RSA","IND","AUS","IND","IND","IND","NZ","RSA"])
rps_batting_2017["Country"] = pd.Series(rps_country_2017, rps_batting_2017.index)
big_data_2017 = big_data_2017.append(rps_batting_2017)

rcb_b_b_f = pd.read_html("http://stats.espncricinfo.com/indian-premier-league-2017/engine/records/averages/batting_bowling_by_team.html?id=11701;team=4340;type=tournament", index_col = 0)
rcb_batting_2017 = rcb_b_b_f[0]
rcb_batting_2017["Team"] = "RCB"
rcb_country_2017 = np.array(["IND","AUS","RSA","IND","IND","WI","IND","IND","IND","AUS","IND","IND","IND","IND","NZ","ENG","WI","IND","IND","IND","AUS"])
rcb_batting_2017["Country"] = pd.Series(rcb_country_2017, rcb_batting_2017.index)
big_data_2017 = big_data_2017.append(rcb_batting_2017)

srh_b_b_f = pd.read_html("http://stats.espncricinfo.com/indian-premier-league-2017/engine/records/averages/batting_bowling_by_team.html?id=11701;team=5143;type=tournament", index_col = 0)
srh_batting_2017 = srh_b_b_f[0]
srh_batting_2017["Team"] = "SRH"
srh_country_2017 = np.array(["AUS","IND","AUS","NZ","IND","IND","IND","IND","AUS","IND","AFG","IND","AFG","ENG","IND","IND","IND","BD","IND"])
srh_batting_2017["Country"] = pd.Series(srh_country_2017, srh_batting_2017.index)
big_data_2017 = big_data_2017.append(srh_batting_2017)

big_data_2017["Season"] = 2017

big_data = big_data_2017

#2016

dd_b_b_f_2016 = pd.read_html("http://stats.espncricinfo.com/indian-premier-league-2016/engine/records/averages/batting_bowling_by_team.html?id=11001;team=4344;type=tournament", index_col = 0)
delhi_batting_2016 = dd_b_b_f_2016[0]
delhi_batting_2016["Team"] = "DD"
dd_country_2016 = np.array(["RSA","RSA","RSA","IND","IND","IND","IND","ENG","WI","IND","IND","RSA","IND","IND","IND","AUS","IND","IND"])
delhi_batting_2016["Country"] = pd.Series(dd_country_2016, delhi_batting_2016.index)
big_data_2016 = delhi_batting_2016

gl_b_b_f_2016 = pd.read_html("http://stats.espncricinfo.com/indian-premier-league-2016/engine/records/averages/batting_bowling_by_team.html?id=11001;team=5845;type=tournament", index_col = 0)
gujarat_batting_2016 = gl_b_b_f_2016[0]
gujarat_batting_2016["Team"] = "GL"
gl_country_2016 = np.array(["AUS","WI","IND","IND","AUS","NZ","IND","IND","WI","IND","IND","IND","IND","RSA","IND","IND","IND","IND","IND"])
gujarat_batting_2016["Country"] = pd.Series(gl_country_2016, gujarat_batting_2016.index)
big_data_2016 = big_data_2016.append(gujarat_batting_2016)

kxip_b_b_f_2016 = pd.read_html("http://stats.espncricinfo.com/indian-premier-league-2016/engine/records/averages/batting_bowling_by_team.html?id=11001;team=4342;type=tournament", index_col = 0)
kxip_batting_2016 = kxip_b_b_f_2016[0]
kxip_batting_2016["Team"] = "KXIP"
kxip_country_2016 = np.array(["AUS","IND","AUS","RSA","IND","IND","IND","AUS","IND","RSA","IND","RSA","IND","IND","IND","RSA","AUS","IND","IND","IND","IND"])
kxip_batting_2016["Country"] = pd.Series(kxip_country_2016, kxip_batting_2016.index)
big_data_2016 = big_data_2016.append(kxip_batting_2016)

kkr_b_b_f_2016 = pd.read_html("http://stats.espncricinfo.com/indian-premier-league-2016/engine/records/averages/batting_bowling_by_team.html?id=11001;team=4341;type=tournament", index_col = 0)
kkr_batting_2016 = kkr_b_b_f_2016[0]
kkr_batting_2016["Team"] = "KKR"
kkr_country_2016 = np.array(["IND","IND","IND","WI","IND","IND","AUS","BD","NZ","IND","IND","IND","WI","WI","RSA","AUS","AUS","IND","IND","IND"])
kkr_batting_2016["Country"] = pd.Series(kkr_country_2016, kkr_batting_2016.index)
big_data_2016 = big_data_2016.append(kkr_batting_2016)

mi_b_b_f_2016 = pd.read_html("http://stats.espncricinfo.com/indian-premier-league-2016/engine/records/averages/batting_bowling_by_team.html?id=11001;team=4346;type=tournament", index_col = 0)
mi_batting_2016 = mi_b_b_f_2016[0]
mi_batting_2016["Team"] = "MI"
mi_country_2016 = np.array(["IND","IND","IND","IND","IND","WI","ENG","NZ","IND","IND","NZ","NZ","IND","WI","IND","IND","IND","IND"])
mi_batting_2016["Country"] = pd.Series(mi_country_2016, mi_batting_2016.index)
big_data_2016 = big_data_2016.append(mi_batting_2016)

rps_b_b_f_2016 = pd.read_html("http://stats.espncricinfo.com/indian-premier-league-2016/engine/records/averages/batting_bowling_by_team.html?id=11001;team=5843;type=tournament", index_col = 0)
rps_batting_2016 = rps_b_b_f_2016[0]
rps_batting_2016["Team"] = "RPS"
rps_country_2016 = np.array(["AUS","IND","IND","ENG","RSA","IND","IND","SL","AUS","AUS","IND","RSA","AUS","AUS","IND","IND","AUS","IND","IND","AUS","IND","IND","IND"])
rps_batting_2016["Country"] = pd.Series(rps_country_2016, rps_batting_2016.index)
big_data_2016 = big_data_2016.append(rps_batting_2016)

rcb_b_b_f_2016 = pd.read_html("http://stats.espncricinfo.com/indian-premier-league-2016/engine/records/averages/batting_bowling_by_team.html?id=11001;team=4340;type=tournament", index_col = 0)
rcb_batting_2016 = rcb_b_b_f_2016[0]
rcb_batting_2016["Team"] = "RCB"
rcb_country_2016 = np.array(["IND","RSA","IND","IND","IND","AUS","WI","IND","AUS","IND","ENG","IND","IND","RSA","AUS","IND","IND","IND","IND","IND","NZ","RSA"])
rcb_batting_2016["Country"] = pd.Series(rcb_country_2016, rcb_batting_2016.index)
big_data_2016 = big_data_2016.append(rcb_batting_2016)

srh_b_b_f_2016 = pd.read_html("http://stats.espncricinfo.com/indian-premier-league-2016/engine/records/averages/batting_bowling_by_team.html?id=11001;team=5143;type=tournament", index_col = 0)
srh_batting_2016 = srh_b_b_f_2016[0]
srh_batting_2016["Team"] = "SRH"
srh_country_2016 = np.array(["AUS","IND","AUS","IND","IND","ENG","IND","NZ","AUS","IND","IND","IND","IND","IND","IND","IND","NZ","BD"])
srh_batting_2016["Country"] = pd.Series(srh_country_2016, srh_batting_2016.index)
big_data_2016 = big_data_2016.append(srh_batting_2016)

big_data_2016["Season"] = 2016

big_data = big_data.append(big_data_2016)

#2015
csk_b_b_f_2015 = pd.read_html("http://stats.espncricinfo.com/indian-premier-league-2015/engine/records/averages/batting_bowling_by_team.html?id=9657;team=4343;type=tournament", index_col = 0)
csk_batting_2015 = csk_b_b_f_2015[0]
csk_batting_2015["Team"] = "CSK"
csk_country_2015 = np.array(["NZ","IND","RSA","WI","IND","WI","AUS","IND","IND","IND","IND","IND","IND","IND"])
csk_batting_2015["Country"] = pd.Series(csk_country_2015, csk_batting_2015.index)
big_data_2015 = csk_batting_2015

dd_b_b_f_2015 = pd.read_html("http://stats.espncricinfo.com/indian-premier-league-2015/engine/records/averages/batting_bowling_by_team.html?id=9657;team=4344;type=tournament", index_col = 0)
dd_batting_2015 = dd_b_b_f_2015[0]
dd_batting_2015["Team"] = "DD"
dd_country_2015 = np.array(["RSA","RSA","RSA","IND","IND","IND","IND","SL","IND","AUS","RSA","IND","IND","IND","IND","IND","IND","AUS","IND","IND"])
dd_batting_2015["Country"] = pd.Series(dd_country_2015, dd_batting_2015.index)
big_data_2015 = big_data_2015.append(dd_batting_2015)

kxip_b_b_f_2015 = pd.read_html("http://stats.espncricinfo.com/indian-premier-league-2015/engine/records/averages/batting_bowling_by_team.html?id=9657;team=4342;type=tournament", index_col = 0)
kxip_batting_2015 = kxip_b_b_f_2015[0]
kxip_batting_2015["Team"] = "KXIP"
kxip_country_2015 = np.array(["RSA","RSA","IND","IND","AUS","IND","IND","AUS","IND","IND","IND","IND","AUS","IND","IND","SL","IND","RSA","IND"])
kxip_batting_2015["Country"] = pd.Series(kxip_country_2015, kxip_batting_2015.index)
big_data_2015 = big_data_2015.append(kxip_batting_2015)

kkr_b_b_f_2015 = pd.read_html("http://stats.espncricinfo.com/indian-premier-league-2015/engine/records/averages/batting_bowling_by_team.html?id=9657;team=4341;type=tournament", index_col = 0)
kkr_batting_2015 = kkr_b_b_f_2015[0]
kkr_batting_2015["Team"] = "KKR"
kkr_country_2015 = np.array(["IND","WI","IND","IND","IND","IND","NED","IND","IND","BD","RSA","AUS","ENG","AUS","RSA","WI","IND"])
kkr_batting_2015["Country"] = pd.Series(kkr_country_2015, kkr_batting_2015.index)
big_data_2015 = big_data_2015.append(kkr_batting_2015)

mi_b_b_f_2015 = pd.read_html("http://stats.espncricinfo.com/indian-premier-league-2015/engine/records/averages/batting_bowling_by_team.html?id=9657;team=4346;type=tournament", index_col = 0)
mi_batting_2015 = mi_b_b_f_2015[0]
mi_batting_2015["Team"] = "MI"
mi_country_2015 = np.array(["IND","WI","WI","NZ","IND","IND","IND","IND","IND","IND","NZ","AUS","IND","IND","SL","IND","IND","RSA","IND","IND"])
mi_batting_2015["Country"] = pd.Series(mi_country_2015, mi_batting_2015.index)
big_data_2015 = big_data_2015.append(mi_batting_2015)

rr_b_b_f_2015 = pd.read_html("http://stats.espncricinfo.com/indian-premier-league-2015/engine/records/averages/batting_bowling_by_team.html?id=9657;team=4345;type=tournament", index_col = 0)
rr_batting_2015 = rr_b_b_f_2015[0]
rr_batting_2015["Team"] = "RR"
rr_country_2015 = np.array(["IND","AUS","RSA","AUS","IND","IND","AUS","IND","IND","NZ","IND","IND","IND","IND","RSA","IND","IND"])
rr_batting_2015["Country"] = pd.Series(rr_country_2015, rr_batting_2015.index)
big_data_2015 = big_data_2015.append(rr_batting_2015)

rcb_b_b_f_2015 = pd.read_html("http://stats.espncricinfo.com/indian-premier-league-2015/engine/records/averages/batting_bowling_by_team.html?id=9657;team=4340;type=tournament", index_col = 0)
rcb_batting_2015 = rcb_b_b_f_2015[0]
rcb_batting_2015["Team"] = "RCB"
rcb_country_2015 = np.array(["RSA","IND","WI","RSA","IND","IND","IND","IND","AUS","IND","IND","AUS","RSA","WI","IND","AUS","IND","IND","IND","IND"])
rcb_batting_2015["Country"] = pd.Series(rcb_country_2015, rcb_batting_2015.index)
big_data_2015 = big_data_2015.append(rcb_batting_2015)

srh_b_b_f_2015 = pd.read_html("http://stats.espncricinfo.com/indian-premier-league-2015/engine/records/averages/batting_bowling_by_team.html?id=9657;team=5143;type=tournament", index_col = 0)
srh_batting_2015 = srh_b_b_f_2015[0]
srh_batting_2015["Team"] = "SRH"
srh_country_2015 = np.array(["AUS","AUS","NZ","ENG","IND","IND","IND","ENG","RSA","IND","IND","IND","IND","IND","IND","IND","NZ","IND"])
srh_batting_2015["Country"] = pd.Series(srh_country_2015, srh_batting_2015.index)
big_data_2015 = big_data_2015.append(srh_batting_2015)

big_data_2015["Season"] = 2015

big_data = big_data.append(big_data_2015)
