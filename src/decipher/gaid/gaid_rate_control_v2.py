# -*- coding:utf-8 -*-
#Desc：gaid按比例回传控制
#Date：2017.4.25
#Author：zhou

import requests,json,unittest,random,datetime
from decipher.gaid.Conf_Public_req_param import *

click_gaid="http://10.200.10.149:8010/v1/click?type=01&p1=30160&p2=3576859&p3=%s&p8=0.37&p9=&p12=%s&p13=400&p26=23&p52=3&p4=%s" \
           "&p5=1662684189370000_1769833153868301&p6=US&p7=a2849f901c3210ca&p11=en&p14=191706&lid=&p15=com.psafe.msuite&p33=000-111-222-333&p34=-1&p35=-1&p36=0" \
           "&p37=0&p38=0&p39=1&p40=10&p48=0&p53=null&p62=1&p28=1"

rate_api='http://10.200.10.149:8010/v1/look/getOfferClickMap?offerid=%s'
rate_source={10444:0.74,
             10342:0.34}

clicks=["http://10.200.10.149:8010/v1/click?type=01&p1=30160&p2=3576859&p3=%s&p8=0.37&p9=&p12=%s&p13=400&p26=23&p52=3&p4=%s" \
           "&p5=1662684189370000_1769833153868301&p6=US&p7=a2849f901c3210ca&p11=en&p14=191706&lid=&p15=com.psafe.msuite&p33=000-111-222-333&p34=-1&p35=-1&p36=0" \
           "&p37=0&p38=0&p39=1&p40=10&p48=0&p53=null&p62=1&p28=1",
        "http://10.200.10.149:8010/v1/click?type=01&p1=30160&p2=3576859&p3=%s&p8=0.37&p9=&p12=%s&p13=400&p26=23&p52=3&p4=%s" \
           "&p5=1662684189370000_1769833153868301&p6=US&p7=a2849f901c3210ca&p11=en&p14=191706&lid=&p15=com.psafe.msuite&p313=000-111-222-333&p34=-1&p35=-1&p36=0" \
           "&p37=0&p38=0&p39=1&p40=10&p48=0&p53=null&p62=1&p28=1"]



class gaid_rate_control(unittest.TestCase):
    def get_offer_rate(self,offer):
        get_content=(requests.get(rate_api%offer)).content
        if 'no this offerid data' not in get_content:
            get_rate=json.loads(get_content)
            rate=get_rate['gaidPerent']
            had_gaid=get_rate['gaidClickNum']
            nogaidNum=get_rate['noGaidClickNum']
            return rate,had_gaid,nogaidNum

    def get_nowtime(self):
        recent_time=datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')
        return recent_time

    def tes_do_click(self):
        for c in xrange(1000):
            # 点击带gaid
            if c<5:
                Reurl=click_gaid%('10444','41447964',random_str())
                header =requests.head(Reurl).headers
                l=header['Location']
                if "error" not in l:
                    l_dic=location_dict_arg(l)
                    if "aff_sub2" in l_dic.keys():
                        params=(l_dic['aff_sub2']).split("_")
                        get_offer_rate=gaid_rate_control.get_offer_rate(self,params[3])   #rate api
                        print "had gaid,直接跳转",c,"source:",params[1],"|offerId",params[3],"|gaid:",l_dic['google_adv_id'],"|rate:",get_offer_rate[0]
            # 点击不带gaid
            if 5<c<=8:
                Reurl=(click_gaid%('10444','41447964',random_str())).replace("&p33=","&p_test=")
                header_data =requests.head(Reurl).headers
                l=header_data['Location']
                if "error" not in l:
                    l_dic=location_dict_arg(l)
                    if "aff_sub2" in l_dic.keys():
                        if "_" in l_dic['aff_sub2']:
                            params=(l_dic['aff_sub2']).split("_")
                            get_offer_rate=gaid_rate_control.get_offer_rate(self,params[3])
                            if int(params[1]) in rate_source.keys():
                                if float(get_offer_rate[0])>=float(rate_source[int(params[1])]):
                                    print "nogaid-rate大于阈值，直接跳转",c,"source:",params[1],"|offerId",params[3],"|rate:",get_offer_rate[0],"|had gaid:",get_offer_rate[1],"|nogaidNum:",get_offer_rate[2]
                                else:
                                    print "nogaid-rate小于阈值,后续开始点击扣量",c,"source:",params[1],"|offerId",params[3],"|rate:",get_offer_rate[0],"|had gaid:",get_offer_rate[1],"|nogaidNum:",get_offer_rate[2]
                            else:
                                print "nogaid-rate小于阈值，点击扣量,优选其他offer",c,"source:",params[1],"|offerId",params[3],"|rate:",get_offer_rate[0],"|had gaid:",get_offer_rate[1],"|nogaidNum:",get_offer_rate[2]
                        else:
                            get_offer_rate=gaid_rate_control.get_offer_rate(self,header_data['Ad-p12'])
                            print "nogaid-rate，点击扣量",c,"offerId",header_data['Ad-p12'],"|pid:",header_data['Ad-p56'],"|rate:",get_offer_rate[0],"|had gaid:",get_offer_rate[1],"|nogaidNum:",get_offer_rate[2]

                    else:
                        print l_dic
                else:
                    print c,l

    def test_ramdom(self):
        have_gaid=0
        no_gaid1=0
        no_gaid2=0
        have1=''
        no_1=''
        no_2=''
        gaid_error=0
        noGaid_error=0
        for c in xrange(50000):
            if c<10000:
                gaid_random=random.sample(clicks,1)
                Reurl=gaid_random[0]%('10444','41447964',random_str())
                if "p33=" in Reurl: # 有gaid
                    header =requests.head(Reurl).headers
                    l=header['Location']
                    if "error" not in l:
                        l_dic=location_dict_arg(l)
                        if "aff_sub2" in l_dic.keys():
                            params=(l_dic['aff_sub2']).split("_")
                            if int(params[1]) in rate_source.keys():
                                have=have_gaid+1
                                have_gaid=have
                                have1=str(params[3])+'_'+str(have_gaid)
                                get_offer_rate0=gaid_rate_control.get_offer_rate(self,params[3])   #rate api
                                if get_offer_rate0:
                                    print gaid_rate_control.get_nowtime(self),c,"had gaid,直接跳转，gaid计数","source:",params[1],"|offerId",params[3],"|gaid:",l_dic['google_adv_id'],\
                                        "|rate:",get_offer_rate0[0],"|had gaid:",get_offer_rate0[1],"|nogaidNum:",get_offer_rate0[2]
                    else:
                        g_error=gaid_error+1
                        gaid_error=g_error
                        print c,"gaid error",l
                else:   #无gaid
                    header =requests.head(Reurl).headers
                    l=header['Location']
                    if "error" not in l:
                        l_dic=location_dict_arg(l)
                        if "aff_sub2" in l_dic.keys():
                            if "_" in l_dic['aff_sub2']:
                                params=(l_dic['aff_sub2']).split("_")
                                #无 gaid 大于gaid阈值，直接跳，nogaid+1
                                if int(params[1]) in rate_source.keys():
                                    no=no_gaid1+1
                                    no_gaid1=no
                                    no_1=str(params[3])+'_'+str(no)
                                    get_offer_rate1=gaid_rate_control.get_offer_rate(self,params[3])
                                    if get_offer_rate1:
                                        if float(get_offer_rate1[0])>=float(rate_source[int(params[1])]):
                                            # pass
                                            print gaid_rate_control.get_nowtime(self),c,"nogaid-rate大于阈值，直接跳转：","source:",params[1],"|offerId",params[3],"|rate:",get_offer_rate1[0],\
                                                "|had gaid:",get_offer_rate1[1],"|nogaidNum:",get_offer_rate1[2]
                                else:
                                    "点击扣量，非gaid必传上游",params

                            else:   #点击扣量
                                no2=no_gaid2+1
                                no_gaid2=no2
                                no_2=str(header['Ad-p12'])+'_'+str(no_gaid2)
                                get_offer_rate2=gaid_rate_control.get_offer_rate(self,header['Ad-p12'])
                                if get_offer_rate2:
                                    print gaid_rate_control.get_nowtime(self),c,"nogaid-rate，点击扣量","offerId",header['Ad-p12'],"|pid:",header['Ad-p56'],"|rate:",get_offer_rate2[0],\
                                        "|had gaid:",get_offer_rate2[1],"|nogaidNum:",get_offer_rate2[2]
                    else:   #无单子可替换，error
                        n_error=noGaid_error+1
                        noGaid_error=n_error
                        print c,"no gaid error",l

        print gaid_rate_control.get_nowtime(self),"gaid:",have1,"no_gaid:",no_1,no_2,"error count:",gaid_error,noGaid_error
if __name__=='__main__':
    unittest.main()





