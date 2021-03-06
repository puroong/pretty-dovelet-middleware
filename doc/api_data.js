define({ "api": [
  {
    "type": "get",
    "url": "/v1/problem",
    "title": "Get dovelet problem",
    "version": "1.0.0",
    "name": "GetProblem",
    "group": "Problem",
    "header": {
      "fields": {
        "Header": [
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "PHPSESSID",
            "description": "<p>Dovelet phpsessid</p>"
          },
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "member_id",
            "description": "<p>Dovelet member_id</p>"
          },
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "member_passwd",
            "description": "<p>Dovelet member_passwd</p>"
          },
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "member_sid",
            "description": "<p>Dovelet member_sid</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Header-Example:",
          "content": "Must send with set-cookie header\n\nSet-Cookie: PHPSESSID=sdafj13123\nSet-Cookie: member_id=dsf324elfsdkj324\nSet-Cookie: member_passwd=2123jfdskljfsdl\nSet-Cookie: member_sid=dfds32432jlrfdslk",
          "type": "String"
        }
      ]
    },
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "title",
            "description": "<p>Problem title</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "problem",
            "description": "<p>Problem html</p>"
          }
        ]
      }
    },
    "error": {
      "fields": {
        "Error 4xx": [
          {
            "group": "Error 4xx",
            "type": "String",
            "optional": false,
            "field": "problem",
            "description": "<p>Dovelet 404 html</p>"
          }
        ]
      }
    },
    "filename": "app/resources/problem.py",
    "groupTitle": "Problem"
  },
  {
    "type": "post",
    "url": "/v1/problem",
    "title": "Submit dovelet problem",
    "version": "1.0.0",
    "name": "SubmitProblem",
    "group": "Problem",
    "header": {
      "fields": {
        "Header": [
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "PHPSESSID",
            "description": "<p>Dovelet phpsessid</p>"
          },
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "member_id",
            "description": "<p>Dovelet member_id</p>"
          },
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "member_passwd",
            "description": "<p>Dovelet member_passwd</p>"
          },
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "member_sid",
            "description": "<p>Dovelet member_sid</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Header-Example:",
          "content": "Must send with set-cookie header\n\nSet-Cookie: PHPSESSID=sdafj13123\nSet-Cookie: member_id=dsf324elfsdkj324\nSet-Cookie: member_passwd=2123jfdskljfsdl\nSet-Cookie: member_sid=dfds32432jlrfdslk",
          "type": "String"
        }
      ]
    },
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "title",
            "description": "<p>Problem title</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "language",
            "description": "<p>Programming language of source code</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "source",
            "description": "<p>Source code submitting</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "result",
            "description": "<p>Result page html</p>"
          }
        ]
      }
    },
    "error": {
      "fields": {
        "Error 4xx": [
          {
            "group": "Error 4xx",
            "type": "String",
            "optional": false,
            "field": "result",
            "description": "<p>Result page html</p>"
          }
        ]
      }
    },
    "filename": "app/resources/problem.py",
    "groupTitle": "Problem"
  },
  {
    "type": "get",
    "url": "/v1/stair/:stair_num",
    "title": "Get stair problems",
    "version": "1.0.0",
    "name": "GetStair",
    "group": "Stair",
    "header": {
      "fields": {
        "Header": [
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "PHPSESSID",
            "description": "<p>Dovelet phpsessid</p>"
          },
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "member_id",
            "description": "<p>Dovelet member_id</p>"
          },
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "member_passwd",
            "description": "<p>Dovelet member_passwd</p>"
          },
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "member_sid",
            "description": "<p>Dovelet member_sid</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Header-Example:",
          "content": "Must send with set-cookie header\n\nSet-Cookie: PHPSESSID=sdafj13123\nSet-Cookie: member_id=dsf324elfsdkj324\nSet-Cookie: member_passwd=2123jfdskljfsdl\nSet-Cookie: member_sid=dfds32432jlrfdslk",
          "type": "String"
        }
      ]
    },
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "stair_num",
            "description": "<p>Number of requesting stair</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Object[]",
            "optional": false,
            "field": "problems",
            "description": "<p>List of problems in a stair</p>"
          }
        ]
      }
    },
    "filename": "app/resources/stair.py",
    "groupTitle": "Stair"
  },
  {
    "type": "get",
    "url": "/v1/me",
    "title": "User profile",
    "version": "1.0.0",
    "name": "GetProfile",
    "group": "User",
    "header": {
      "fields": {
        "Header": [
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "PHPSESSID",
            "description": "<p>Dovelet phpsessid</p>"
          },
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "member_id",
            "description": "<p>Dovelet member_id</p>"
          },
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "member_passwd",
            "description": "<p>Dovelet member_passwd</p>"
          },
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "member_sid",
            "description": "<p>Dovelet member_sid</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Header-Example:",
          "content": "Must send with set-cookie header\n\nSet-Cookie: PHPSESSID=sdafj13123\nSet-Cookie: member_id=dsf324elfsdkj324\nSet-Cookie: member_passwd=2123jfdskljfsdl\nSet-Cookie: member_sid=dfds32432jlrfdslk",
          "type": "String"
        }
      ]
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "profile",
            "description": "<p>User Profile html</p>"
          }
        ]
      }
    },
    "error": {
      "fields": {
        "Error 4xx": [
          {
            "group": "Error 4xx",
            "type": "String",
            "optional": false,
            "field": "profile",
            "description": ""
          }
        ]
      }
    },
    "filename": "app/resources/user.py",
    "groupTitle": "User"
  },
  {
    "type": "post",
    "url": "/v1/login",
    "title": "Login",
    "version": "1.0.0",
    "name": "Login",
    "group": "User",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "id",
            "description": "<p>Dovelet user id</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "passwd",
            "description": "<p>Dovelet user password</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Boolean",
            "optional": false,
            "field": "success",
            "description": "<p>True</p>"
          },
          {
            "group": "Success 200",
            "type": "Object",
            "optional": false,
            "field": "cookies",
            "description": "<p>Dovelet cookies</p>"
          }
        ]
      }
    },
    "error": {
      "fields": {
        "Error 4xx": [
          {
            "group": "Error 4xx",
            "type": "Object",
            "optional": false,
            "field": "cookies",
            "description": "<p>Empty object</p>"
          }
        ]
      }
    },
    "filename": "app/resources/user.py",
    "groupTitle": "User"
  },
  {
    "type": "get",
    "url": "/v1/logout",
    "title": "Logout",
    "version": "1.0.0",
    "name": "Logout",
    "group": "User",
    "header": {
      "fields": {
        "Header": [
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "PHPSESSID",
            "description": "<p>Dovelet phpsessid</p>"
          },
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "member_id",
            "description": "<p>Dovelet member_id</p>"
          },
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "member_passwd",
            "description": "<p>Dovelet member_passwd</p>"
          },
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "member_sid",
            "description": "<p>Dovelet member_sid</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Header-Example:",
          "content": "Must send with set-cookie header\n\nSet-Cookie: PHPSESSID=sdafj13123\nSet-Cookie: member_id=dsf324elfsdkj324\nSet-Cookie: member_passwd=2123jfdskljfsdl\nSet-Cookie: member_sid=dfds32432jlrfdslk",
          "type": "String"
        }
      ]
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Boolean",
            "optional": false,
            "field": "success",
            "description": "<p>True</p>"
          }
        ]
      }
    },
    "error": {
      "fields": {
        "Error 4xx": [
          {
            "group": "Error 4xx",
            "type": "Boolean",
            "optional": false,
            "field": "success",
            "description": ""
          }
        ]
      }
    },
    "filename": "app/resources/user.py",
    "groupTitle": "User"
  }
] });
