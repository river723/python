(function(e) {
    var t = function() {
        function e() {}
        return e.prototype.getUrlInfo = function(e, t) {
            var n = {
                url: "",
                path: "",
                params: {}
            }
                , i = [];
            t || (t = []),
            Array.isArray(t) || (t = [t]),
                t.forEach((function(e) {
                        for (var t in e)
                            i.push(t + "=" + e[t]),
                                n.params[t] = e[t]
                    }
                ));
            var r = e.indexOf("?");
            return r > 0 ? (n.path = e.substr(0, r),
                e.substr(r + 1).split("&").forEach((function(e) {
                        var t = e.indexOf("=");
                        if (t <= 0)
                            i.push(e);
                        else {
                            var r = e.substr(0, t)
                                , o = decodeURIComponent(e.substr(t + 1));
                            n.params[r] || (n.params[r] = o,
                                i.push(r + "=" + o))
                        }
                    }
                ))) : n.path = e,
                n.url = n.path,
            i.length && (n.url += "?" + i.join("&")),
                n
        }
            ,
            e.prototype.copyObject = function(e) {
                if (e)
                    return JSON.parse(JSON.stringify(e))
            }
            ,
            e.prototype.uuid = function(t, n) {
                void 0 === t && (t = 16),
                void 0 === n && (n = !1),
                !n && t < 16 && (console.error("uuid useCase=false 时 len 不能小于 16"),
                    t = 16),
                n && t < 12 && (console.error("uuid useCase=true 时 len 不能小于 12"),
                    t = 12);
                var i = ((new Date).getTime() + 1e14).toString();
                return i += ("000" + (++e.uuidCount).toString()).substr(-3, 3),
                    i = n ? parseInt(i).to62() : parseInt(i).toString(36),
                    i += this.randomStr(t),
                    i = i.substr(0, t),
                    i
            }
            ,
            e.prototype.random = function(e, t) {
                return void 0 === e && (e = 0),
                void 0 === t && (t = 1e4),
                    Math.round(Math.random() * (t - e) + e)
            }
            ,
            e.prototype.randomStr = function(e) {
                for (var t = [], n = 0; n < e; n++)
                    t.push(this.random(0, 35).toString(36));
                return t.join("")
            }
            ,
            e.prototype.definePropertyHide = function(e, t) {
                Object.defineProperty(e, t, {
                    configurable: !0,
                    enumerable: !1,
                    writable: !0
                })
            }
            ,
            e.prototype.each = function(e, t) {
                if ("number" == typeof e) {
                    for (var n = 0; n < e; n++)
                        if (!1 === t(n, n))
                            return e
                } else if ("object" == typeof e) {
                    for (var i in e)
                        if ("function" != typeof e[i] && !1 === t(e[i], i))
                            return e
                } else if (Array.isArray(e))
                    for (n = 0; n < e.length; n++)
                        if (!1 === t(e[n], n))
                            break;
                return e
            }
            ,
            e.uuidCount = 0,
            e.instantiation = function() {
                return e._instantiation || (e._instantiation = new e),
                    e._instantiation
            }
            ,
            e
    }();
    e.Utils = t,
        function(e) {
            var t, n = function() {
                function n() {
                    var t = this;
                    this.utils = e.instantiation,
                        this.log = console.log,
                        this.mapList = [],
                        this.mapHash = {},
                        this.getNextIndex = 0,
                        this.list = [],
                        this.instantiation = function() {
                            return t
                        }
                        ,
                        this.utils().definePropertyHide(this, "mapList"),
                        this.utils().definePropertyHide(this, "mapHash"),
                        this.utils().definePropertyHide(this, "getNextIndex"),
                        this.utils().definePropertyHide(this, "timeoutRemoveIndex")
                }
                return n.prototype.pushJsonDict = function(e) {
                    var t = this;
                    this.utils().each(e, (function(e, n) {
                            t.push(n, e)
                        }
                    ))
                }
                    ,
                    n.prototype.push = function(e, n) {
                        var i = this.mapHash[e];
                        return i ? (console.log("Map push 时主键重复:" + e, n),
                            i.value) : (i = new t.MapItem(e,n),
                            this.mapList.push(i),
                            this.list.push(n),
                            this.mapHash[e] = i,
                            n)
                    }
                    ,
                    n.prototype.pushByArray = function(e, t) {
                        var n = this;
                        return void 0 === t && (t = "id"),
                            Array.isArray(e) ? (e.forEach((function(e) {
                                    e[t] && n.push(e[t], e)
                                }
                            )),
                                this) : this
                    }
                    ,
                    n.prototype.pop = function() {
                        var e = this.mapList.pop();
                        return this.list.pop(),
                            delete this.mapHash[e.key],
                            e.value
                    }
                    ,
                    n.prototype.setListObject = function(e) {
                        this.list = e
                    }
                    ,
                    n.prototype.unshift = function(e, n) {
                        this.mapHash[e] && console.log("Map unshift 时主键重复:" + e);
                        var i = new t.MapItem(e,n);
                        return this.mapList.unshift(i),
                            this.list.unshift(n),
                            this.mapHash[e] = i,
                            this
                    }
                    ,
                    n.prototype.shift = function() {
                        var e = this.mapList.shift();
                        if (e)
                            return this.list.shift(),
                                delete this.mapHash[e.key],
                                e.value
                    }
                    ,
                    n.prototype.remove = function(e) {
                        var t = this.mapHash[e];
                        if (t)
                            return this.mapList.remove(t),
                                this.list.remove(t.value),
                                delete this.mapHash[e],
                                t.value
                    }
                    ,
                    n.prototype.removes = function(e) {
                        var t = this;
                        return Array.isArray(e) ? (e.forEach((function(e) {
                                t.remove(e)
                            }
                        )),
                            this) : this
                    }
                    ,
                    n.prototype.get = function(e, t, n) {
                        if (this.mapHash[e])
                            return t && t(this.mapHash[e].value),
                                this.mapHash[e].value;
                        n && n()
                    }
                    ,
                    n.prototype.getFirst = function(e, t) {
                        var n = void 0;
                        return this.mapList.length > 0 && (n = this.mapList[0].value),
                        n && e && e(n),
                        !n && t && t(),
                            n
                    }
                    ,
                    n.prototype.getLast = function(e, t) {
                        var n = void 0;
                        return this.mapList.length > 0 && (n = this.mapList[this.mapList.length - 1].value),
                        n && e && e(n),
                        !n && t && t(),
                            n
                    }
                    ,
                    n.prototype.getNext = function(e, t) {
                        var n = void 0;
                        return this.mapList.length > 0 && (this.getNextIndex >= this.mapList.length && (this.getNextIndex = 0),
                            n = this.mapList[this.getNextIndex].value,
                            this.getNextIndex++),
                        n && e && e(n),
                        !n && t && t(),
                            n
                    }
                    ,
                    n.prototype.update = function(e, n) {
                        var i = new t.MapItem(e,n)
                            , r = this.mapHash[e];
                        if (r) {
                            var o = this.mapList.indexOf(r);
                            o >= 0 && (this.mapList[o] = i)
                        }
                        var a = this.list.indexOf(n);
                        return a >= 0 && (this.list[a] = n),
                            this.mapHash[e] = i,
                            this
                    }
                    ,
                    n.prototype.find = function(e) {
                        var t = this;
                        void 0 === e && (e = {});
                        var n = [];
                        return this.each((function(i, r) {
                                t.utils().each(e, (function(e, t) {
                                        i[t] === i && n.push(i)
                                    }
                                ))
                            }
                        )),
                            n
                    }
                    ,
                    n.prototype.findByAttr = function(e, t) {
                        var n = void 0;
                        return this.each((function(i, r) {
                                if (i[e] === t)
                                    return n = i,
                                        !1
                            }
                        )),
                            n
                    }
                    ,
                    Object.defineProperty(n.prototype, "listItem", {
                        get: function() {
                            var e = [];
                            return this.mapList.forEach((function(t) {
                                    e.push(t)
                                }
                            )),
                                e
                        },
                        enumerable: !1,
                        configurable: !0
                    }),
                    Object.defineProperty(n.prototype, "hash", {
                        get: function() {
                            return this.mapHash
                        },
                        enumerable: !1,
                        configurable: !0
                    }),
                    Object.defineProperty(n.prototype, "length", {
                        get: function() {
                            return this.mapList.length
                        },
                        enumerable: !1,
                        configurable: !0
                    }),
                    n.prototype.each = function(e) {
                        var t = Object(s["c"])(this.mapList);
                        this.utils().each(t, (function(t, n) {
                                return e(t.value, t.key, n)
                            }
                        ))
                    }
                    ,
                    n.prototype.splice = function(e, t) {
                        void 0 === t && (t = this.length);
                        var n = [];
                        t > this.length - e && (t = this.length - e);
                        for (var i = e; i < t; i++) {
                            var r = this.mapList[i];
                            delete this.mapHash[r.key],
                                n.push(r.value)
                        }
                        return this.mapList.splice(e, t),
                            this.list.splice(e, t),
                            n
                    }
                    ,
                    n.prototype.clear = function() {
                        this.mapList = [],
                            this.mapHash = {},
                            this.list.splice(0, this.list.length),
                            this.getNextIndex = 0
                    }
                    ,
                    n.prototype.startTimeoutRemove = function(e, t, n) {
                        var i = this;
                        return void 0 === n && (n = 1e3),
                            this.stopTimeoutRemove(),
                            this.timeoutRemoveIndex = setInterval((function() {
                                    i.execTimeoutRemove(e, t)
                                }
                            ), n),
                            this
                    }
                    ,
                    n.prototype.execTimeoutRemove = function(e, t) {
                        var n = this
                            , i = []
                            , r = (new Date).getTime();
                        this.each((function(n, o, a) {
                                n[t] && "number" == typeof n[t] && r - n[t] > e && i.push(o)
                            }
                        )),
                            i.forEach((function(e) {
                                    n.remove(e)
                                }
                            ))
                    }
                    ,
                    n.prototype.stopTimeoutRemove = function() {
                        return clearInterval(this.timeoutRemoveIndex),
                            this
                    }
                    ,
                    n
            }();
            e.Map = n,
                function(e) {
                    var t = function() {
                        function e(e, t) {
                            this.key = e,
                                this.value = t
                        }
                        return e
                    }();
                    e.MapItem = t
                }(t = e.UtilsMap || (e.UtilsMap = {}))
        }(t = e.Utils || (e.Utils = {}))
}