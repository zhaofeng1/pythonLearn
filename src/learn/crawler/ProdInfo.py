'''
Created on 2017年1月4日

@author: Administrator
'''
class ProdInfo:
    prodTitle = ''
    imgUrls = ''
    details = ''
    rp = ''
    sebelum = ''
    diskon = ''
    descTitle = ''
    descHtml = ''

    def get_prod_title(self):
        return self.__prodTitle


    def get_img_urls(self):
        return self.__imgUrls


    def get_details(self):
        return self.__details


    def get_rp(self):
        return self.__rp


    def get_sebelum(self):
        return self.__sebelum


    def get_diskon(self):
        return self.__diskon


    def get_desc_title(self):
        return self.__descTitle


    def get_desc_html(self):
        return self.__descHtml


    def set_prod_title(self, value):
        self.__prodTitle = value


    def set_img_urls(self, value):
        self.__imgUrls = value


    def set_details(self, value):
        self.__details = value


    def set_rp(self, value):
        self.__rp = value


    def set_sebelum(self, value):
        self.__sebelum = value


    def set_diskon(self, value):
        self.__diskon = value


    def set_desc_title(self, value):
        self.__descTitle = value


    def set_desc_html(self, value):
        self.__descHtml = value


    def del_prod_title(self):
        del self.__prodTitle


    def del_img_urls(self):
        del self.__imgUrls


    def del_details(self):
        del self.__details


    def del_rp(self):
        del self.__rp


    def del_sebelum(self):
        del self.__sebelum


    def del_diskon(self):
        del self.__diskon


    def del_desc_title(self):
        del self.__descTitle


    def del_desc_html(self):
        del self.__descHtml

    prodTitle = property(get_prod_title, set_prod_title, del_prod_title, "prodTitle's docstring")
    imgUrls = property(get_img_urls, set_img_urls, del_img_urls, "imgUrls's docstring")
    details = property(get_details, set_details, del_details, "details's docstring")
    rp = property(get_rp, set_rp, del_rp, "rp's docstring")
    sebelum = property(get_sebelum, set_sebelum, del_sebelum, "sebelum's docstring")
    diskon = property(get_diskon, set_diskon, del_diskon, "diskon's docstring")
    descTitle = property(get_desc_title, set_desc_title, del_desc_title, "descTitle's docstring")
    descHtml = property(get_desc_html, set_desc_html, del_desc_html, "descHtml's docstring")
    
    