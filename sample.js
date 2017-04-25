/**
 * Created by mio4kon on 17/4/25.
 */

var TAG = '[MOCK_ENV]';
var mysql = require('mysql');

module.exports = {
    summary: 'a rule to modify response',
    *beforeSendResponse(requestDetail, responseDetail) {
        console.log(TAG, "监听到的URL:", requestDetail.url);
       
        const newResponse = responseDetail.response;
        return new Promise((resolve, reject) => {
           newResponse.body = '111';
           resolve({response: newResponse});
           
        });
    },
};




