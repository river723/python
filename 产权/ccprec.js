window=global;
(function(e) {
        function t(t) {
            for (var r, i, u = t[0], c = t[1], s = t[2], l = 0, d = []; l < u.length; l++)
                i = u[l],
                Object.prototype.hasOwnProperty.call(a, i) && a[i] && d.push(a[i][0]),
                    a[i] = 0;
            for (r in c)
                Object.prototype.hasOwnProperty.call(c, r) && (e[r] = c[r]);
            f && f(t);
            while (d.length)
                d.shift()();
            return o.push.apply(o, s || []),
                n()
        }
        function n() {
            for (var e, t = 0; t < o.length; t++) {
                for (var n = o[t], r = !0, i = 1; i < n.length; i++) {
                    var u = n[i];
                    0 !== a[u] && (r = !1)
                }
                r && (o.splice(t--, 1),
                    e = c(c.s = n[0]))
            }
            return e
        }
        var r = {}
            , i = {
            navCqzr: 0
        }
            , a = {
            navCqzr: 0
        }
            , o = [];
        function u(e) {
            return c.p + "static_assets/js/" + ({}[e] || e) + "." + {
                "chunk-2c124d8d": "13d9a4b5",
                "chunk-0604b86a": "b2489847",
                "chunk-53670e35": "0f4b7029"
            }[e] + ".js"
        }
        function c(t) {
            if (r[t])
                return r[t].exports;
            var n = r[t] = {
                i: t,
                l: !1,
                exports: {}
            };
            return e[t].call(n.exports, n, n.exports, c),
                n.l = !0,
                n.exports
        }
        c.e = function(e) {
            var t = []
                , n = {
                "chunk-2c124d8d": 1,
                "chunk-0604b86a": 1,
                "chunk-53670e35": 1
            };
            i[e] ? t.push(i[e]) : 0 !== i[e] && n[e] && t.push(i[e] = new Promise((function(t, n) {
                    for (var r = "static_assets/css/" + ({}[e] || e) + "." + {
                        "chunk-2c124d8d": "bdf3f1b4",
                        "chunk-0604b86a": "c6444c7e",
                        "chunk-53670e35": "46534a9b"
                    }[e] + ".css", a = c.p + r, o = document.getElementsByTagName("link"), u = 0; u < o.length; u++) {
                        var s = o[u]
                            , l = s.getAttribute("data-href") || s.getAttribute("href");
                        if ("stylesheet" === s.rel && (l === r || l === a))
                            return t()
                    }
                    var d = document.getElementsByTagName("style");
                    for (u = 0; u < d.length; u++) {
                        s = d[u],
                            l = s.getAttribute("data-href");
                        if (l === r || l === a)
                            return t()
                    }
                    var f = document.createElement("link");
                    f.rel = "stylesheet",
                        f.type = "text/css",
                        f.onload = t,
                        f.onerror = function(t) {
                            var r = t && t.target && t.target.src || a
                                , o = new Error("Loading CSS chunk " + e + " failed.\n(" + r + ")");
                            o.code = "CSS_CHUNK_LOAD_FAILED",
                                o.request = r,
                                delete i[e],
                                f.parentNode.removeChild(f),
                                n(o)
                        }
                        ,
                        f.href = a;
                    var p = document.getElementsByTagName("head")[0];
                    p.appendChild(f)
                }
            )).then((function() {
                    i[e] = 0
                }
            )));
            var r = a[e];
            if (0 !== r)
                if (r)
                    t.push(r[2]);
                else {
                    var o = new Promise((function(t, n) {
                            r = a[e] = [t, n]
                        }
                    ));
                    t.push(r[2] = o);
                    var s, l = document.createElement("script");
                    l.charset = "utf-8",
                        l.timeout = 120,
                    c.nc && l.setAttribute("nonce", c.nc),
                        l.src = u(e);
                    var d = new Error;
                    s = function(t) {
                        l.onerror = l.onload = null,
                            clearTimeout(f);
                        var n = a[e];
                        if (0 !== n) {
                            if (n) {
                                var r = t && ("load" === t.type ? "missing" : t.type)
                                    , i = t && t.target && t.target.src;
                                d.message = "Loading chunk " + e + " failed.\n(" + r + ": " + i + ")",
                                    d.name = "ChunkLoadError",
                                    d.type = r,
                                    d.request = i,
                                    n[1](d)
                            }
                            a[e] = void 0
                        }
                    }
                    ;
                    var f = setTimeout((function() {
                            s({
                                type: "timeout",
                                target: l
                            })
                        }
                    ), 12e4);
                    l.onerror = l.onload = s,
                        document.head.appendChild(l)
                }
            return Promise.all(t)
        }
            ,
            c.m = e,
            c.c = r,
            c.d = function(e, t, n) {
                c.o(e, t) || Object.defineProperty(e, t, {
                    enumerable: !0,
                    get: n
                })
            }
            ,
            c.r = function(e) {
                "undefined" !== typeof Symbol && Symbol.toStringTag && Object.defineProperty(e, Symbol.toStringTag, {
                    value: "Module"
                }),
                    Object.defineProperty(e, "__esModule", {
                        value: !0
                    })
            }
            ,
            c.t = function(e, t) {
                if (1 & t && (e = c(e)),
                8 & t)
                    return e;
                if (4 & t && "object" === typeof e && e && e.__esModule)
                    return e;
                var n = Object.create(null);
                if (c.r(n),
                    Object.defineProperty(n, "default", {
                        enumerable: !0,
                        value: e
                    }),
                2 & t && "string" != typeof e)
                    for (var r in e)
                        c.d(n, r, function(t) {
                            return e[t]
                        }
                            .bind(null, r));
                return n
            }
            ,
            c.n = function(e) {
                var t = e && e.__esModule ? function() {
                            return e["default"]
                        }
                        : function() {
                            return e
                        }
                ;
                return c.d(t, "a", t),
                    t
            }
            ,
            c.o = function(e, t) {
                return Object.prototype.hasOwnProperty.call(e, t)
            }
            ,
            c.p = "/",
            c.oe = function(e) {
                throw console.error(e),
                    e
            }
        ;
        var s = window["webpackJsonp"] = window["webpackJsonp"] || []
            , l = s.push.bind(s);
        s.push = t,
            s = s.slice();
        for (var d = 0; d < s.length; d++)
            t(s[d]);
        var f = l;
        o.push([20, "chunk-common"]),
            n()
    }
)({

}
)

var random = function (e, t) {
    return void 0 === e && (e = 0),
    void 0 === t && (t = 1e4),
        Math.floor(Math.random() * (t - e) + e)
}
var randomStr = function (e) {
    for (var t = [], n = 0; n < e; n++)
        t.push(random(0, 35).toString(36));
    return t.join("")
}

uuid = function (t, n) {
    void 0 === t && (t = 16),
    void 0 === n && (n = !1),
    !n && t < 16 && (console.error("uuid useCase=false 时 len 不能小于 16"),
        t = 16),
    n && t < 12 && (console.error("uuid useCase=true 时 len 不能小于 12"),
        t = 12);

    var i = ((new Date).getTime() + 1e14).toString();
    return i += ("000" + (++e_uuidCount).toString()).substr(-3, 3),
        i = n ? parseInt(i).to62() : parseInt(i).toString(36),
        i += randomStr(t),
        i = i.substr(0, t),
        i
}

var e_uuidCount=0
var stringChangeASCIINumberArrs = function (e) {
    for (var t = [], n = 0; n < e.length; n++)
        t.push(e.charCodeAt(n));
    return t
}
var pubPassNum = []
var pubPass = "BX1o65CoobwcDP33iQW6ld1OyIPsNzF1"
pubPassNum = stringChangeASCIINumberArrs(pubPass)
encryptCode = function (e) {

    for (var t = encodeURI(e), n = [], i = 0, r = "", o = random(16, 32), a = randomStr(o), s = stringChangeASCIINumberArrs(a), l = 0, c = 0, u = 0, h = 0; h < t.length; h++)
        i = t.charCodeAt(h),
        l == pubPassNum.length && (l = 0),
            i += pubPassNum[l],
            l++,
        c == s.length && (c = 0),
            i += s[c],
            c++,
            u += i,
        u > 65535 && (u -= 65535),
            r = i.toString(36),
            r = ("00" + r).substr(-2, 2),
        1 == r.length && (r = "0" + r),
            n.push(r);
    var d = "";
    return d = u.toString(36),
        d = ("0000" + r).substr(-4, 4),
        n.unshift(a),
        n.unshift(o.toString(36)),
        n.unshift(d),
        n.join("")
}

decryptCode = function(e) {
    var t = ""
        , n = 0
        , i = ""
        , r = []
        , o = []
        , a = 0
        , s = 0;
    t = e.substr(4, 1),
        n = parseInt(t, 36),
        i = e.substr(5, n),
        r = stringChangeASCIINumberArrs(i),
        t = e.substr(5 + n, e.length - 5 - n);
    for (var l = "", c = 0, u = 0, h = 0; h < t.length / 2; h++)
        l = t.substr(u, 2),
            u += 2,
            c = parseInt(l, 36),
        s == r.length && (s = 0),
            c -= r[s],
            s++,
        a == pubPass.length && (a = 0),
            c -= pubPassNum[a],
            a++,
            l = String.fromCharCode(c),
            o.push(l);
    return t = o.join(""),
        t = decodeURI(t),
        t
}

function main123(page) {
    clientKey =uuid()
    o = {
        "id": uuid(),
        "projectKey": "honsan_cloud_ccprec",
        "clientKey": clientKey,
        "token": null,
        "clientDailyData": {},
        "acts": [
            {
                "id": uuid(),
                "fullPath": "/ccprec.com.cn.web/client/info/cqweb_nonphy_cqzr",
                "args": [page, 20, null]
            }
        ]
    }

    a = JSON.stringify(o)
    console.log(a)
    console.log('----------------------')

    t = JSON.stringify(a)
    s = encryptCode(t)
    console.log(s)
    return s
}

ma = main123(1)
// console.log('----------------------')
// jm=decryptCode(ma)
// console.log(jm)