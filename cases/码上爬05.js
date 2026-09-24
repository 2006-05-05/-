const CryptoJS = require('crypto-js')

function encrypt(_0x277028) {
    let key = CryptoJS['enc']['Utf8']['parse']('jo8j9wGw%6HbxfFn'),
    iv = CryptoJS['enc']['Utf8']['parse']('0123456789ABCDEF');

    let _0x2703a2 = CryptoJS['enc']['Utf8']['parse'](_0x277028),
        _0x50fcf0 = CryptoJS['AES']['encrypt'](_0x2703a2, key, {
            'mode': CryptoJS['mode']['CBC'],
            'padding': CryptoJS['pad']['Pkcs7'],
            'iv': iv
        });
    return _0x50fcf0['ciphertext']['toString'](CryptoJS['enc']['Hex']);
}


function loadPage(pageNumber){
    const timestamp = new Date().getTime();
    const params = {
        page: pageNumber,
        _ts: timestamp,
    };
    let x = encrypt(JSON.stringify(params));
    return {
        xl:x
    };
}