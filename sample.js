/**
 * Created by mio4kon on 17/4/25.
 */

var TAG = '[MOCK_ENV]';
var mysql = require('mysql');

module.exports = {
    summary: 'a rule to modify response',
    *beforeSendResponse(requestDetail, responseDetail) {
        console.log(TAG, "监听到的URL:", requestDetail.url);
        let sql = 'SELECT * FROM mock WHERE INSTR(\'' + requestDetail.url + '\',url) >0 AND mock_type = \'' + 'success' + '\'';
        const newResponse = responseDetail.response;
        return new Promise((resolve, reject) => {
            let conn = connectMockEnv()
            conn.query(sql, function (err, rows) {
                console.log(TAG, rows);
                if (rows.length > 0) {
                    newResponse.body = rows[0].body;
                    newResponse.statusCode = rows[0].status_code;
                    resolve({response: newResponse});
                } else {
                    resolve({response: newResponse});
                }
                disconnectMockEnv(conn);
            });
        });
    },
};


function connectMockEnv() {
    var connection = mysql.createConnection({
        host: 'localhost',
        user: 'root',
        password: 'root',
        port: '3306',
        database: 'test',
    });

    connection.connect();
    return connection;
}

function disconnectMockEnv(conn) {
    conn.end()
}


