class UrlBuilder:
    
    base = 'https://www.ncei.noaa.gov/cdo-web/api/v2/'


    def __init__(self, endpoint, options):
        self.endpoint = endpoint
        self.options = options

    def endpoint(self):
        return self.endpoint

    def genUrl(self):
        str = '' # this is what is appended to the url called by request.py
        if self.resource == '':
            if self.endpoint == 'datasets':
                str = 'datasets/'
                str += "?"
                #DataTypeId -- here the datatype ids to be selected are parsed -- check the notes page that has the orders of the search query parameters
                if len(self.options) > 0: #array length check
                    if self.options[0] is not []:
                        datatypeids = ''
                        for i in self.options[0]:
                            datatypeids += ('&' + 'datatypeid=' + i)
                        str += datatypeids

                #LocationId -- here the locatoin ids that are desired are filtered upon     
                if len(self.options) > 1: #array length check
                    if self.options[1] is not []:
                        locationids = ''
                        for i in self.options[1]:
                            locationids += ('&' + 'locationid=' + i)
                        str += locationids

                #StationID -- here the station ids that are desired are filtered upon     
                if len(self.options) > 2: #array length check
                    if self.options[2] is not []:
                        stationids = ''
                        for i in self.options[2]:
                            stationids += ('&' + 'stationid=' +  i)
                        str += stationids

                #StartDate -- this will filter data that  is taken after the start date is specified
                if len(self.options) > 3: #array length check
                    if self.options[3] is not []:
                        startdate = '&startdate=' + self.options[3]
                        str += startdate

                #EndDate -- this will filter data that is from before the end date
                if len(self.options) > 4: #array length check
                    if self.options[4] is not []:
                        enddate = '&enddate=' + self.options[4]
                        str += enddate

                #SortField -- choose which field to sort by -- DOES HAVE DEFAULT BEHAVIOR !!! ENSURE SORTING IS CORRECT FOR USE 
                if len(self.options) > 5: #array length check
                    if self.options[5] is not []:
                        sortfield = '&sortfield=' + self.options[5]
                        str += sortfield

                #SortOrder -- chose to sort selecton ascending or descending on the sort attr. specified above
                if len(self.options) > 6: #array length check
                    if self.options[6] is not []:
                        sortorder = '&sortorder=' + self.options[6]

                #Limit -- How many results to be returned. MAX 1000 -- check in place
                if len(self.options) > 7: #array length check
                    if self.options[7] is not []:
                        if int(self.options[7]) > 1000:
                            limit = '&limit=1000'
                        else:
                            limit = '&limit=' + self.options[7]

                #Offset -- what index to start the results from
                if len(self.options[8]) > 8: #array length check
                    if self.options is not []:
                        offset = '&offset=' + self.options[8] # THIS CAN GIVE ERROR IF NUMBER IS HIGHER THAN NUMBER OF RECORDS 
                                                              # NOTHING IS RETURNED ON THIS ERROR

                str = str[1:]
    
        else:
            str += self.resource
        
        #return statement for both branches    
        return self.base + str


