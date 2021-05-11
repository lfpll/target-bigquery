schema_simple_1 = '{ "type": "SCHEMA", "stream": "simple_stream", "schema": { "properties": { "id": { "type": [ "null", "string" ] }, "name": { "type": [ "null", "string" ] }, "value": { "type": [ "null", "integer" ] }, "ratio": { "type": [ "null", "number" ] }, "timestamp": { "type": "string", "format": "date-time" }, "date": { "type": "string", "format": "date" }, "geo": { "type": "string", "format": "bq-geography" } }, "type": [ "null", "object" ] }, "key_properties": [ "id" ], "bookmark_properties": [ "date" ] }'


# schema_nested_1 - method 2 of schema conversion ("simplify and convert") failed

    # Simplifying function

        # input:
        # { "age": { "type": [ "null", "integer", "string" ] }

        # output of simplifying:
        # 'age': {'anyOf': [{'type': ['integer', 'null']}, {'type': ['string', 'null']}]}

        #anyOf appears this causes our conversion to fail
        # issue solved. Prioritization of data types is implemented.


schema_nested_1 =  '{ "type": "SCHEMA", "stream": "nested_stream", "schema": { "properties": { "account_id": { "type": [ "null", "string" ] }, "account_name": { "type": [ "null", "string" ] }, "action_values": { "items": { "properties": { "1d_click": { "type": [ "null", "number" ] }, "1d_view": { "type": [ "null", "number" ] }, "28d_click": { "type": [ "null", "number" ] }, "28d_view": { "type": [ "null", "number" ] }, "7d_click": { "type": [ "null", "number" ] }, "7d_view": { "type": [ "null", "number" ] }, "action_destination": { "type": [ "null", "string" ] }, "action_target_id": { "type": [ "null", "string" ] }, "action_type": { "type": [ "null", "string" ] }, "value": { "type": [ "null", "number" ] } }, "type": [ "null", "object" ] }, "type": [ "null", "array" ] }, "actions": { "items": { "properties": { "1d_click": { "type": [ "null", "number" ] }, "1d_view": { "type": [ "null", "number" ] }, "28d_click": { "type": [ "null", "number" ] }, "28d_view": { "type": [ "null", "number" ] }, "7d_click": { "type": [ "null", "number" ] }, "7d_view": { "type": [ "null", "number" ] }, "action_destination": { "type": [ "null", "string" ] }, "action_target_id": { "type": [ "null", "string" ] }, "action_type": { "type": [ "null", "string" ] }, "value": { "type": [ "null", "number" ] } }, "type": [ "null", "object" ] }, "type": [ "null", "array" ] }, "ad_id": { "type": [ "null", "string" ] }, "ad_name": { "type": [ "null", "string" ] }, "adset_id": { "type": [ "null", "string" ] }, "adset_name": { "type": [ "null", "string" ] }, "age": { "type": [ "null", "integer", "string" ] }, "campaign_id": { "type": [ "null", "string" ] }, "campaign_name": { "type": [ "null", "string" ] }, "canvas_avg_view_percent": { "type": [ "null", "number" ] }, "canvas_avg_view_time": { "type": [ "null", "number" ] }, "clicks": { "type": [ "null", "integer" ] }, "conversion_rate_ranking": { "type": [ "null", "string" ] }, "cost_per_action_type": { "items": { "properties": { "action_type": { "type": [ "null", "string" ] }, "value": { "type": [ "null", "string" ] } }, "type": [ "null", "object" ] }, "type": [ "null", "array" ] }, "cost_per_inline_link_click": { "type": [ "null", "number" ] }, "cost_per_inline_post_engagement": { "type": [ "null", "number" ] }, "cost_per_unique_action_type": { "items": { "properties": { "action_type": { "type": [ "null", "string" ] }, "value": { "type": [ "null", "string" ] } }, "type": [ "null", "object" ] }, "type": [ "null", "array" ] }, "cost_per_unique_click": { "type": [ "null", "number" ] }, "cost_per_unique_inline_link_click": { "type": [ "null", "number" ] }, "cpc": { "type": [ "null", "number" ] }, "cpm": { "type": [ "null", "number" ] }, "cpp": { "type": [ "null", "number" ] }, "ctr": { "type": [ "null", "number" ] }, "date_start": { "format": "date-time", "type": [ "null", "string" ] }, "date_stop": { "format": "date-time", "type": [ "null", "string" ] }, "engagement_rate_ranking": { "type": [ "null", "string" ] }, "frequency": { "type": [ "null", "number" ] }, "gender": { "type": [ "null", "string" ] }, "impressions": { "type": [ "null", "integer" ] }, "inline_link_click_ctr": { "type": [ "null", "number" ] }, "inline_link_clicks": { "type": [ "null", "integer" ] }, "inline_post_engagement": { "type": [ "null", "integer" ] }, "objective": { "type": [ "null", "string" ] }, "outbound_clicks": { "items": { "properties": { "1d_click": { "type": [ "null", "number" ] }, "1d_view": { "type": [ "null", "number" ] }, "28d_click": { "type": [ "null", "number" ] }, "28d_view": { "type": [ "null", "number" ] }, "7d_click": { "type": [ "null", "number" ] }, "7d_view": { "type": [ "null", "number" ] }, "action_destination": { "type": [ "null", "string" ] }, "action_target_id": { "type": [ "null", "string" ] }, "action_type": { "type": [ "null", "string" ] }, "value": { "type": [ "null", "number" ] } }, "type": [ "null", "object" ] }, "type": [ "null", "array" ] }, "quality_ranking": { "type": [ "null", "string" ] }, "reach": { "type": [ "null", "integer" ] }, "social_spend": { "type": [ "null", "number" ] }, "spend": { "type": [ "null", "number" ] }, "unique_actions": { "items": { "properties": { "1d_click": { "type": [ "null", "number" ] }, "1d_view": { "type": [ "null", "number" ] }, "28d_click": { "type": [ "null", "number" ] }, "28d_view": { "type": [ "null", "number" ] }, "7d_click": { "type": [ "null", "number" ] }, "7d_view": { "type": [ "null", "number" ] }, "action_destination": { "type": [ "null", "string" ] }, "action_target_id": { "type": [ "null", "string" ] }, "action_type": { "type": [ "null", "string" ] }, "value": { "type": [ "null", "number" ] } }, "type": [ "null", "object" ] }, "type": [ "null", "array" ] }, "unique_clicks": { "type": [ "null", "integer" ] }, "unique_ctr": { "type": [ "null", "number" ] }, "unique_inline_link_click_ctr": { "type": [ "null", "number" ] }, "unique_inline_link_clicks": { "type": [ "null", "integer" ] }, "unique_link_clicks_ctr": { "type": [ "null", "number" ] }, "video_30_sec_watched_actions": { "items": { "properties": { "1d_click": { "type": [ "null", "number" ] }, "1d_view": { "type": [ "null", "number" ] }, "28d_click": { "type": [ "null", "number" ] }, "28d_view": { "type": [ "null", "number" ] }, "7d_click": { "type": [ "null", "number" ] }, "7d_view": { "type": [ "null", "number" ] }, "action_destination": { "type": [ "null", "string" ] }, "action_target_id": { "type": [ "null", "string" ] }, "action_type": { "type": [ "null", "string" ] }, "value": { "type": [ "null", "number" ] } }, "type": [ "null", "object" ] }, "type": [ "null", "array" ] }, "video_p100_watched_actions": { "items": { "properties": { "1d_click": { "type": [ "null", "number" ] }, "1d_view": { "type": [ "null", "number" ] }, "28d_click": { "type": [ "null", "number" ] }, "28d_view": { "type": [ "null", "number" ] }, "7d_click": { "type": [ "null", "number" ] }, "7d_view": { "type": [ "null", "number" ] }, "action_destination": { "type": [ "null", "string" ] }, "action_target_id": { "type": [ "null", "string" ] }, "action_type": { "type": [ "null", "string" ] }, "value": { "type": [ "null", "number" ] } }, "type": [ "null", "object" ] }, "type": [ "null", "array" ] }, "video_p25_watched_actions": { "items": { "properties": { "1d_click": { "type": [ "null", "number" ] }, "1d_view": { "type": [ "null", "number" ] }, "28d_click": { "type": [ "null", "number" ] }, "28d_view": { "type": [ "null", "number" ] }, "7d_click": { "type": [ "null", "number" ] }, "7d_view": { "type": [ "null", "number" ] }, "action_destination": { "type": [ "null", "string" ] }, "action_target_id": { "type": [ "null", "string" ] }, "action_type": { "type": [ "null", "string" ] }, "value": { "type": [ "null", "number" ] } }, "type": [ "null", "object" ] }, "type": [ "null", "array" ] }, "video_p50_watched_actions": { "items": { "properties": { "1d_click": { "type": [ "null", "number" ] }, "1d_view": { "type": [ "null", "number" ] }, "28d_click": { "type": [ "null", "number" ] }, "28d_view": { "type": [ "null", "number" ] }, "7d_click": { "type": [ "null", "number" ] }, "7d_view": { "type": [ "null", "number" ] }, "action_destination": { "type": [ "null", "string" ] }, "action_target_id": { "type": [ "null", "string" ] }, "action_type": { "type": [ "null", "string" ] }, "value": { "type": [ "null", "number" ] } }, "type": [ "null", "object" ] }, "type": [ "null", "array" ] }, "video_p75_watched_actions": { "items": { "properties": { "1d_click": { "type": [ "null", "number" ] }, "1d_view": { "type": [ "null", "number" ] }, "28d_click": { "type": [ "null", "number" ] }, "28d_view": { "type": [ "null", "number" ] }, "7d_click": { "type": [ "null", "number" ] }, "7d_view": { "type": [ "null", "number" ] }, "action_destination": { "type": [ "null", "string" ] }, "action_target_id": { "type": [ "null", "string" ] }, "action_type": { "type": [ "null", "string" ] }, "value": { "type": [ "null", "number" ] } }, "type": [ "null", "object" ] }, "type": [ "null", "array" ] }, "video_play_curve_actions": { "items": { "properties": { "action_type": { "type": [ "null", "string" ] }, "value": { "items": { "type": [ "null", "integer" ] }, "type": [ "null", "array" ] } }, "type": [ "null", "object" ] }, "type": [ "null", "array" ] }, "website_ctr": { "items": { "properties": { "action_destination": { "type": [ "null", "string" ] }, "action_target_id": { "type": [ "null", "string" ] }, "action_type": { "type": [ "null", "string" ] }, "value": { "type": [ "null", "number" ] } }, "type": [ "null", "object" ] }, "type": [ "null", "array" ] } }, "type": [ "null", "object" ] }, "key_properties": [ "campaign_id", "adset_id", "ad_id", "date_start", "age", "gender" ], "bookmark_properties": [ "date_start" ] }'



# made-up schema - collection of columns with anyOf
test_schema_collection_anyOf_problem_column =  """{ "type": "SCHEMA", "stream": "nested_stream", "schema": { "properties": 

{ 
  
    "test_column_no_anyOf": { "items": { "properties": { "action_destination": { "type": [ "null", "string" ] }, "action_target_id": { "type": [ "null", "string" ] }, "action_type": { "type": [ "null", "string" ] }, "value": { "type": [ "null", "number" ] } }, "type": [ "null", "object" ] }, "type": [ "null", "array" ] },


    "BiddingScheme": {"anyOf": [{"type": ["null", "object"], "additionalProperties": false, "properties": {"Type": {"type": ["null", "string"]}, "InheritedBidStrategyType": {"type": ["null", "string"]}}}, {"type": ["null", "object"], "additionalProperties": false, "properties": {"Type": {"type": ["null", "string"]}}}, {"type": ["null", "object"], "additionalProperties": false, "properties": {"Type": {"type": ["null", "string"]}, "MaxCpc": {"type": ["null", "object"], "additionalProperties": false, "properties": {"Amount": {"type": ["null", "number"]}}}}}, {"type": ["null", "object"], "additionalProperties": false, "properties": {"Type": {"type": ["null", "string"]}, "MaxCpc": {"type": ["null", "object"], "additionalProperties": false, "properties": {"Amount": {"type": ["null", "number"]}}}}}, {"type": ["null", "object"], "additionalProperties": false, "properties": {"Type": {"type": ["null", "string"]}, "MaxCpc": {"type": ["null", "object"], "additionalProperties": false, "properties": {"Amount": {"type": ["null", "number"]}}}, "TargetCpa": {"type": ["null", "number"]}}}, {"type": ["null", "object"], "additionalProperties": false, "properties": {"Type": {"type": ["null", "string"]}, "TargetRoas": {"type": ["null", "number"]}}}, {"type": ["null", "object"], "additionalProperties": false, "properties": {"Type": {"type": ["null", "string"]}, "MaxCpc": {"type": ["null", "object"], "additionalProperties": false, "properties": {"Amount": {"type": ["null", "number"]}}}, "TargetRoas": {"type": ["null", "number"]}}}, {"type": ["null", "object"], "additionalProperties": false, "properties": {"Type": {"type": ["null", "string"]}, "MaxCpc": {"type": ["null", "object"], "additionalProperties": false, "properties": {"Amount": {"type": ["null", "number"]}}}}}, {"type": ["null", "object"], "additionalProperties": false, "properties": {"Type": {"type": ["null", "string"]}}}, {"type": ["null", "object"], "additionalProperties": false, "properties": {"Type": {"type": ["null", "string"]}, "MaxCpc": {"type": ["null", "object"], "additionalProperties": false, "properties": {"Amount": {"type": ["null", "number"]}}}, "TargetAdPosition": {"type": ["null", "string"]}, "TargetImpressionShare": {"type": ["null", "number"]}}}, {"type": ["null", "object"], "additionalProperties": false, "properties": {"Type": {"type": ["null", "string"]}}}]}, 

    "Settings": {"type": ["null", "object"], "properties": {"Setting": {"type": ["null", "array"], "items": {"anyOf": [{"type": ["null", "object"], "additionalProperties": false, "properties": {"Type": {"type": ["null", "string"]}, "Details": {"type": ["null", "object"], "properties": {"TargetSettingDetail": {"type": ["null", "array"], "items": {"type": ["null", "object"], "additionalProperties": false, "properties": {"CriterionTypeGroup": {"type": ["null", "string"]}, "TargetAndBid": {"type": ["boolean"]}}}}}}}}, {"type": ["null", "object"], "additionalProperties": false, "properties": {"Type": {"type": ["null", "string"]}, "LocalInventoryAdsEnabled": {"type": ["null", "boolean"]}, "Priority": {"type": ["null", "integer"]}, "SalesCountryCode": {"type": ["null", "string"]}, "StoreId": {"type": ["null", "integer"]}}}, {"type": ["null", "object"], "additionalProperties": false, "properties": {"Type": {"type": ["null", "string"]}, "BidBoostValue": {"type": ["null", "number"]}, "BidMaxValue": {"type": ["null", "number"]}, "BidOption": {"type": ["null", "string"]}}}, {"type": ["null", "object"], "additionalProperties": false, "properties": {"Type": {"type": ["null", "string"]}, "DomainName": {"type": ["null", "string"]}, "Language": {"type": ["null", "string"]}, "PageFeedIds": {"type": ["null", "object"], "properties": {"long": {"type": ["null", "array"], "items": {"type": "integer"}}}}, "Source": {"type": ["null", "string"]}}}, {"type": ["null", "object"], "additionalProperties": false, "properties": {"Type": {"type": ["null", "string"]}}}]}}}}, 


    "discount_codes": {            "anyOf": [              {                "type": "array",                "items": {                  "type": "object",                  "additionalProperties": false,                  "properties": {                    "amount": {                      "type": [                        "null",                        "number"                      ]                    },                    "code": {                      "type": [                        "null",                        "string"                      ]                    },                    "type": {                      "type": [                        "null",                        "string"                      ]                    }                  }                }              },              {                "type": "null"              }            ]          }, 



    "line_items": {            "anyOf": [              {                "type": "array",                "items": {                  "type": "object",                  "additionalProperties": false,                  "properties": {                    "grams": {                      "type": [                        "null",                        "integer"                      ]                    },                    "images": {                      "type": [                        "null",                        "object"                      ],                      "additionalProperties": false,                      "properties": {                        "large": {                          "type": [                            "null",                            "string"                          ]                        },                        "medium": {                          "type": [                            "null",                            "string"                          ]                        },                        "original": {                          "type": [                            "null",                            "string"                          ]                        },                        "small": {                          "type": [                            "null",                            "string"                          ]                        }                      }                    },                    "price": {                      "type": [                        "null",                        "number"                      ],                      "multipleOf": 1e-08                    },                    "properties": {                      "anyOf": [                        {                          "type": "array",                          "items": {                            "type": "object",                            "additionalProperties": false,                            "properties": {                              "name": {                                "type": [                                  "null",                                  "string"                                ]                              },                              "value": {                                "type": [                                  "null",                                  "string"                                ]                              }                            }                          }                        },                        {                          "type": "null"                        }                      ]                    },                    "quantity": {                      "type": [                        "null",                        "integer"                      ]                    },                    "shopify_product_id": {                      "type": [                        "null",                        "string"                      ]                    },                    "shopify_variant_id": {                      "type": [                        "null",                        "string"                      ]                    },                    "sku": {                      "type": [                        "null",                        "string"                      ]                    },                    "subscription_id": {                      "type": [                        "null",                        "string"                      ]                    },                    "title": {                      "type": [                        "null",                        "string"                      ]                    },                    "variant_title": {                      "type": [                        "null",                        "string"                      ]                    },                    "vendor": {                      "type": [                        "null",                        "string"                      ]                    }                  }                }              },              {                "type": "null"              }            ]          }, 



    "shipping_lines": {            "anyOf": [              {                "type": "array",                "items": {                  "type": "object",                  "additionalProperties": false,                  "properties": {                    "code": {                      "type": [                        "null",                        "string"                      ]                    },                    "price": {                      "type": [                        "null",                        "number"                      ]                    },                    "title": {                      "type": [                        "null",                        "string"                      ]                    }                  }                }              },              {                "type": "null"              }            ]          }, 


    "tax_lines": {            "anyOf": [              {                "type": "array",                "items": {                  "type": "object",                  "additionalProperties": false,                  "properties": {                    "code": {                      "type": [                        "null",                        "string"                      ]                    },                    "price": {                      "type": [                        "null",                        "number"                      ]                    },                    "title": {                      "type": [                        "null",                        "string"                      ]                    }                  }                }              },              {                "type": "null"              }            ]          },


    "note_attributes": {            "anyOf": [              {                "type": "array",                "items": {                  "type": "object",                  "additionalProperties": false,                  "properties": {                    "name": {                      "type": [                        "null",                        "string"                      ]                    },                    "value": {                      "type": [                        "null",                        "string"                      ]                    }                  }                }              },              {                "type": "null"              }            ]          },

    "simplification_stage_adds_anyOf": { "type": [ "null", "integer", "string" ] }

   

    
}, "type": [ "null", "object" ] }, "key_properties": [ "campaign_id", "adset_id", "ad_id", "date_start", "age", "gender" ], "bookmark_properties": [ "date_start" ] }"""



# if a column has "items", but doesn't have "properties" inside, it  created an issue while re-writing schema.py to make it simpler. Issue has been handled.
schema_nested_1_subset_items_problem =  '{ "type": "SCHEMA", "stream": "nested_stream", "schema": { "properties": {"video_play_curve_actions": { "items": { "properties": { "action_type": { "type": [ "null", "string" ] }, "problem_field": { "items": { "type": [ "null", "integer" ] }, "type": [ "null", "array" ] } }, "type": [ "null", "object" ] }, "type": [ "null", "array" ] }, "website_ctr": { "items": { "properties": { "action_destination": { "type": [ "null", "string" ] }, "action_target_id": { "type": [ "null", "string" ] }, "action_type": { "type": [ "null", "string" ] }, "value": { "type": [ "null", "number" ] } }, "type": [ "null", "object" ] }, "type": [ "null", "array" ] } }, "type": [ "null", "object" ] }, "key_properties": [ "campaign_id", "adset_id", "ad_id", "date_start", "age", "gender" ], "bookmark_properties": [ "date_start" ] }'


schema_nested_2 = '{"type": "SCHEMA", "stream": "campaigns", "schema": {"type": ["null", "object"], "additionalProperties": false, "properties": {"AudienceAdsBidAdjustment": {"type": ["null", "integer"]}, "BiddingScheme": {"anyOf": [{"type": ["null", "object"], "additionalProperties": false, "properties": {"Type": {"type": ["null", "string"]}, "InheritedBidStrategyType": {"type": ["null", "string"]}}}, {"type": ["null", "object"], "additionalProperties": false, "properties": {"Type": {"type": ["null", "string"]}}}, {"type": ["null", "object"], "additionalProperties": false, "properties": {"Type": {"type": ["null", "string"]}, "MaxCpc": {"type": ["null", "object"], "additionalProperties": false, "properties": {"Amount": {"type": ["null", "number"]}}}}}, {"type": ["null", "object"], "additionalProperties": false, "properties": {"Type": {"type": ["null", "string"]}, "MaxCpc": {"type": ["null", "object"], "additionalProperties": false, "properties": {"Amount": {"type": ["null", "number"]}}}}}, {"type": ["null", "object"], "additionalProperties": false, "properties": {"Type": {"type": ["null", "string"]}, "MaxCpc": {"type": ["null", "object"], "additionalProperties": false, "properties": {"Amount": {"type": ["null", "number"]}}}, "TargetCpa": {"type": ["null", "number"]}}}, {"type": ["null", "object"], "additionalProperties": false, "properties": {"Type": {"type": ["null", "string"]}, "TargetRoas": {"type": ["null", "number"]}}}, {"type": ["null", "object"], "additionalProperties": false, "properties": {"Type": {"type": ["null", "string"]}, "MaxCpc": {"type": ["null", "object"], "additionalProperties": false, "properties": {"Amount": {"type": ["null", "number"]}}}, "TargetRoas": {"type": ["null", "number"]}}}, {"type": ["null", "object"], "additionalProperties": false, "properties": {"Type": {"type": ["null", "string"]}, "MaxCpc": {"type": ["null", "object"], "additionalProperties": false, "properties": {"Amount": {"type": ["null", "number"]}}}}}, {"type": ["null", "object"], "additionalProperties": false, "properties": {"Type": {"type": ["null", "string"]}}}, {"type": ["null", "object"], "additionalProperties": false, "properties": {"Type": {"type": ["null", "string"]}, "MaxCpc": {"type": ["null", "object"], "additionalProperties": false, "properties": {"Amount": {"type": ["null", "number"]}}}, "TargetAdPosition": {"type": ["null", "string"]}, "TargetImpressionShare": {"type": ["null", "number"]}}}, {"type": ["null", "object"], "additionalProperties": false, "properties": {"Type": {"type": ["null", "string"]}}}]}, "BudgetType": {"type": ["null", "string"]}, "DailyBudget": {"type": ["null", "number"]}, "ExperimentId": {"type": ["null", "integer"]}, "FinalUrlSuffix": {"type": ["null", "string"]}, "ForwardCompatibilityMap": {"type": ["null", "object"], "properties": {"KeyValuePairOfstringstring": {"type": ["null", "array"], "items": {"type": ["null", "object"], "additionalProperties": false, "properties": {"key": {"type": ["null", "string"]}, "value": {"type": ["null", "string"]}}}}}}, "Id": {"type": ["null", "integer"]}, "Name": {"type": ["null", "string"]}, "Status": {"type": ["null", "string"]}, "SubType": {"type": ["null", "string"]}, "TimeZone": {"type": ["null", "string"]}, "TrackingUrlTemplate": {"type": ["null", "string"]}, "UrlCustomParameters": {"type": ["null", "object"], "additionalProperties": false, "properties": {"Parameters": {"type": ["null", "object"], "properties": {"CustomParameter": {"type": ["null", "array"], "items": {"type": ["null", "object"], "additionalProperties": false, "properties": {"Key": {"type": ["null", "string"]}, "Value": {"type": ["null", "string"]}}}}}}}}, "CampaignType": {"type": ["null", "string"]}, "Settings": {"type": ["null", "object"], "properties": {"Setting": {"type": ["null", "array"], "items": {"anyOf": [{"type": ["null", "object"], "additionalProperties": false, "properties": {"Type": {"type": ["null", "string"]}, "Details": {"type": ["null", "object"], "properties": {"TargetSettingDetail": {"type": ["null", "array"], "items": {"type": ["null", "object"], "additionalProperties": false, "properties": {"CriterionTypeGroup": {"type": ["null", "string"]}, "TargetAndBid": {"type": ["boolean"]}}}}}}}}, {"type": ["null", "object"], "additionalProperties": false, "properties": {"Type": {"type": ["null", "string"]}, "LocalInventoryAdsEnabled": {"type": ["null", "boolean"]}, "Priority": {"type": ["null", "integer"]}, "SalesCountryCode": {"type": ["null", "string"]}, "StoreId": {"type": ["null", "integer"]}}}, {"type": ["null", "object"], "additionalProperties": false, "properties": {"Type": {"type": ["null", "string"]}, "BidBoostValue": {"type": ["null", "number"]}, "BidMaxValue": {"type": ["null", "number"]}, "BidOption": {"type": ["null", "string"]}}}, {"type": ["null", "object"], "additionalProperties": false, "properties": {"Type": {"type": ["null", "string"]}, "DomainName": {"type": ["null", "string"]}, "Language": {"type": ["null", "string"]}, "PageFeedIds": {"type": ["null", "object"], "properties": {"long": {"type": ["null", "array"], "items": {"type": "integer"}}}}, "Source": {"type": ["null", "string"]}}}, {"type": ["null", "object"], "additionalProperties": false, "properties": {"Type": {"type": ["null", "string"]}}}]}}}}, "BudgetId": {"type": ["null", "integer"]}, "Languages": {"type": ["null", "object"], "properties": {"string": {"type": ["null", "array"], "items": {"type": "string"}}}}, "AdScheduleUseSearcherTimeZone": {"type": ["null", "boolean"]}}}, "key_properties": ["Id"]}'


schema_nested_3_shopify = '{    "type":"SCHEMA",    "stream":"orders",    "schema": {        "properties": {          "address_id": {            "type": [              "null",              "string"            ]          },          "address_is_active": {            "type": [              "null",              "boolean"            ]          },          "billing_address": {            "properties": {              "address1": {                "type": [                  "null",                  "string"                ]              },              "address2": {                "type": [                  "null",                  "string"                ]              },              "city": {                "type": [                  "null",                  "string"                ]              },              "company": {                "type": [                  "null",                  "string"                ]              },              "country": {                "type": [                  "null",                  "string"                ]              },              "first_name": {                "type": [                  "null",                  "string"                ]              },              "last_name": {                "type": [                  "null",                  "string"                ]              },              "phone": {                "type": [                  "null",                  "string"                ]              },              "province": {                "type": [                  "null",                  "string"                ]              },              "zip": {                "type": [                  "null",                  "string"                ]              }            },            "type": [              "null",              "object"            ],            "additionalProperties": false          },          "charge_id": {            "type": [              "null",              "string"            ]          },          "charge_status": {            "type": [              "null",              "string"            ]          },          "created_at": {            "format": "date-time",            "type": [              "null",              "string"            ]          },          "customer_id": {            "type": [              "null",              "string"            ]          },          "discount_codes": {            "anyOf": [              {                "type": "array",                "items": {                  "type": "object",                  "additionalProperties": false,                  "properties": {                    "amount": {                      "type": [                        "null",                        "number"                      ]                    },                    "code": {                      "type": [                        "null",                        "string"                      ]                    },                    "type": {                      "type": [                        "null",                        "string"                      ]                    }                  }                }              },              {                "type": "null"              }            ]          },          "email": {            "type": [              "null",              "string"            ]          },          "first_name": {            "type": [              "null",              "string"            ]          },          "hash": {            "type": [              "null",              "string"            ]          },          "id": {            "type": [              "null",              "string"            ]          },          "is_prepaid": {            "type": [              "null",              "boolean"            ]          },          "last_name": {            "type": [              "null",              "string"            ]          },          "line_items": {            "anyOf": [              {                "type": "array",                "items": {                  "type": "object",                  "additionalProperties": false,                  "properties": {                    "grams": {                      "type": [                        "null",                        "integer"                      ]                    },                    "images": {                      "type": [                        "null",                        "object"                      ],                      "additionalProperties": false,                      "properties": {                        "large": {                          "type": [                            "null",                            "string"                          ]                        },                        "medium": {                          "type": [                            "null",                            "string"                          ]                        },                        "original": {                          "type": [                            "null",                            "string"                          ]                        },                        "small": {                          "type": [                            "null",                            "string"                          ]                        }                      }                    },                    "price": {                      "type": [                        "null",                        "number"                      ],                      "multipleOf": 1e-08                    },                    "properties": {                      "anyOf": [                        {                          "type": "array",                          "items": {                            "type": "object",                            "additionalProperties": false,                            "properties": {                              "name": {                                "type": [                                  "null",                                  "string"                                ]                              },                              "value": {                                "type": [                                  "null",                                  "string"                                ]                              }                            }                          }                        },                        {                          "type": "null"                        }                      ]                    },                    "quantity": {                      "type": [                        "null",                        "integer"                      ]                    },                    "shopify_product_id": {                      "type": [                        "null",                        "string"                      ]                    },                    "shopify_variant_id": {                      "type": [                        "null",                        "string"                      ]                    },                    "sku": {                      "type": [                        "null",                        "string"                      ]                    },                    "subscription_id": {                      "type": [                        "null",                        "string"                      ]                    },                    "title": {                      "type": [                        "null",                        "string"                      ]                    },                    "variant_title": {                      "type": [                        "null",                        "string"                      ]                    },                    "vendor": {                      "type": [                        "null",                        "string"                      ]                    }                  }                }              },              {                "type": "null"              }            ]          },          "note": {            "type": [              "null",              "string"            ]          },          "note_attributes": {            "anyOf": [              {                "type": "array",                "items": {                  "type": "object",                  "additionalProperties": false,                  "properties": {                    "name": {                      "type": [                        "null",                        "string"                      ]                    },                    "value": {                      "type": [                        "null",                        "string"                      ]                    }                  }                }              },              {                "type": "null"              }            ]          },          "payment_processor": {            "type": [              "null",              "string"            ]          },          "processed_at": {            "format": "date-time",            "type": [              "null",              "string"            ]          },          "scheduled_at": {            "format": "date-time",            "type": [              "null",              "string"            ]          },          "shipped_date": {            "format": "date-time",            "type": [              "null",              "string"            ]          },          "shipping_address": {            "properties": {              "address1": {                "type": [                  "null",                  "string"                ]              },              "address2": {                "type": [                  "null",                  "string"                ]              },              "city": {                "type": [                  "null",                  "string"                ]              },              "company": {                "type": [                  "null",                  "string"                ]              },              "country": {                "type": [                  "null",                  "string"                ]              },              "first_name": {                "type": [                  "null",                  "string"                ]              },              "last_name": {                "type": [                  "null",                  "string"                ]              },              "phone": {                "type": [                  "null",                  "string"                ]              },              "province": {                "type": [                  "null",                  "string"                ]              },              "zip": {                "type": [                  "null",                  "string"                ]              }            },            "type": [              "null",              "object"            ],            "additionalProperties": false          },          "shipping_date": {            "format": "date-time",            "type": [              "null",              "string"            ]          },          "shipping_lines": {            "anyOf": [              {                "type": "array",                "items": {                  "type": "object",                  "additionalProperties": false,                  "properties": {                    "code": {                      "type": [                        "null",                        "string"                      ]                    },                    "price": {                      "type": [                        "null",                        "number"                      ]                    },                    "title": {                      "type": [                        "null",                        "string"                      ]                    }                  }                }              },              {                "type": "null"              }            ]          },          "shopify_cart_token": {            "type": [              "null",              "string"            ]          },          "shopify_customer_id": {            "type": [              "null",              "string"            ]          },          "shopify_id": {            "type": [              "null",              "string"            ]          },          "shopify_order_id": {            "type": [              "null",              "string"            ]          },          "shopify_order_number": {            "type": [              "null",              "string"            ]          },          "status": {            "type": [              "null",              "string"            ]          },          "subtotal_price": {            "type": [              "null",              "number"            ]          },          "tags": {            "type": [              "null",              "string"            ]          },          "tax_lines": {            "anyOf": [              {                "type": "array",                "items": {                  "type": "object",                  "additionalProperties": false,                  "properties": {                    "code": {                      "type": [                        "null",                        "string"                      ]                    },                    "price": {                      "type": [                        "null",                        "number"                      ]                    },                    "title": {                      "type": [                        "null",                        "string"                      ]                    }                  }                }              },              {                "type": "null"              }            ]          },          "total_discounts": {            "multipleOf": 1e-08,            "type": [              "null",              "number"            ]          },          "total_line_items_price": {            "multipleOf": 1e-08,            "type": [              "null",              "number"            ]          },          "total_price": {            "type": [              "null",              "number"            ]          },          "total_refunds": {            "multipleOf": 1e-08,            "type": [              "null",              "number"            ]          },          "total_tax": {            "multipleOf": 1e-08,            "type": [              "null",              "number"            ]          },          "total_weight": {            "type": [              "null",              "integer"            ]          },          "transaction_id": {            "type": [              "null",              "string"            ]          },          "type": {            "type": [              "null",              "string"            ]          },          "updated_at": {            "format": "date-time",            "type": [              "null",              "string"            ]          }        },        "type": "object",        "additionalProperties": false      },    "key_properties":[       "Id"    ] }'

HubSpot_contact_lists_schema_original = """{
    "streams": [
        {
            "stream": "contact_lists",
            "tap_stream_id": "contact_lists",
            "schema": {
                "type": "object",
                "properties": {
                    "portalId": {
                        "type": [
                            "null",
                            "integer"
                        ]
                    },
                    "listId": {
                        "type": [
                            "null",
                            "integer"
                        ]
                    },
                    "internalListId": {
                        "type": [
                            "null",
                            "integer"
                        ]
                    },
                    "createdAt": {
                        "type": [
                            "null",
                            "string"
                        ],
                        "format": "date-time"
                    },
                    "updatedAt": {
                        "type": [
                            "null",
                            "string"
                        ],
                        "format": "date-time"
                    },
                    "name": {
                        "type": [
                            "null",
                            "string"
                        ]
                    },
                    "listType": {
                        "type": [
                            "null",
                            "string"
                        ]
                    },
                    "parentId": {
                        "type": [
                            "null",
                            "integer"
                        ]
                    },
                    "authorId": {
                        "type": [
                            "null",
                            "integer"
                        ]
                    },
                    "filters": {
                        "type": [
                            "null",
                            "array"
                        ],
                        "items": {
                            "type": [
                                "null",
                                "array"
                            ],
                            "items": {
                                "type": [
                                    "null",
                                    "object"
                                ],
                                "properties": {
                                    "withinTimeMode": {
                                        "type": [
                                            "null",
                                            "string"
                                        ]
                                    },
                                    "filterFamily": {
                                        "type": [
                                            "null",
                                            "string"
                                        ]
                                    },
                                    "operator": {
                                        "type": [
                                            "null",
                                            "string"
                                        ]
                                    },
                                    "type": {
                                        "type": [
                                            "null",
                                            "string"
                                        ]
                                    },
                                    "property": {
                                        "type": [
                                            "null",
                                            "string"
                                        ]
                                    },
                                    "value": {
                                        "type": [
                                            "null",
                                            "string"
                                        ]
                                    },
                                    "checkPastVersions": {
                                        "type": [
                                            "null",
                                            "boolean"
                                        ]
                                    }
                                }
                            }
                        }
                    },
                    "metaData": {
                        "type": [
                            "null",
                            "object"
                        ],
                        "properties": {
                            "size": {
                                "type": [
                                    "null",
                                    "integer"
                                ]
                            },
                            "lastSizeChangeAt": {
                                "type": [
                                    "null",
                                    "string"
                                ],
                                "format": "date-time"
                            },
                            "processing": {
                                "type": [
                                    "null",
                                    "string"
                                ]
                            },
                            "lastProcessingStateChangeAt": {
                                "type": [
                                    "null",
                                    "string"
                                ],
                                "format": "date-time"
                            },
                            "error": {
                                "type": [
                                    "null",
                                    "string"
                                ]
                            },
                            "listReferencesCount": {
                                "type": [
                                    "null",
                                    "integer"
                                ]
                            },
                            "parentFolderId": {
                                "type": [
                                    "null",
                                    "string"
                                ]
                            }
                        }
                    },
                    "archived": {
                        "type": [
                            "null",
                            "boolean"
                        ]
                    },
                    "dynamic": {
                        "type": [
                            "null",
                            "boolean"
                        ]
                    },
                    "readOnly": {
                        "type": [
                            "null",
                            "boolean"
                        ]
                    },
                    "limitExempt": {
                        "type": [
                            "null",
                            "boolean"
                        ]
                    },
                    "deleteable": {
                        "type": [
                            "null",
                            "boolean"
                        ]
                    }
                }
            },
            "metadata": [
                {
                    "breadcrumb": [],
                    "metadata": {
                        "table-key-properties": [
                            "listId"
                        ],
                        "forced-replication-method": "INCREMENTAL",
                        "valid-replication-keys": [
                            "updatedAt"
                        ],
                        "selected": true
                    }
                },
                {
                    "breadcrumb": [
                        "properties",
                        "portalId"
                    ],
                    "metadata": {
                        "inclusion": "available",
                        "selected": true
                    }
                },
                {
                    "breadcrumb": [
                        "properties",
                        "listId"
                    ],
                    "metadata": {
                        "inclusion": "automatic"
                    }
                },
                {
                    "breadcrumb": [
                        "properties",
                        "internalListId"
                    ],
                    "metadata": {
                        "inclusion": "available",
                        "selected": true
                    }
                },
                {
                    "breadcrumb": [
                        "properties",
                        "createdAt"
                    ],
                    "metadata": {
                        "inclusion": "available",
                        "selected": true
                    }
                },
                {
                    "breadcrumb": [
                        "properties",
                        "updatedAt"
                    ],
                    "metadata": {
                        "inclusion": "automatic"
                    }
                },
                {
                    "breadcrumb": [
                        "properties",
                        "name"
                    ],
                    "metadata": {
                        "inclusion": "available",
                        "selected": true
                    }
                },
                {
                    "breadcrumb": [
                        "properties",
                        "listType"
                    ],
                    "metadata": {
                        "inclusion": "available",
                        "selected": true
                    }
                },
                {
                    "breadcrumb": [
                        "properties",
                        "parentId"
                    ],
                    "metadata": {
                        "inclusion": "available",
                        "selected": true
                    }
                },
                {
                    "breadcrumb": [
                        "properties",
                        "authorId"
                    ],
                    "metadata": {
                        "inclusion": "available",
                        "selected": true
                    }
                },
                {
                    "breadcrumb": [
                        "properties",
                        "filters"
                    ],
                    "metadata": {
                        "inclusion": "available",
                        "selected": true
                    }
                },
                {
                    "breadcrumb": [
                        "properties",
                        "metaData"
                    ],
                    "metadata": {
                        "inclusion": "available",
                        "selected": true
                    }
                },
                {
                    "breadcrumb": [
                        "properties",
                        "archived"
                    ],
                    "metadata": {
                        "inclusion": "available",
                        "selected": true
                    }
                },
                {
                    "breadcrumb": [
                        "properties",
                        "dynamic"
                    ],
                    "metadata": {
                        "inclusion": "available",
                        "selected": true
                    }
                },
                {
                    "breadcrumb": [
                        "properties",
                        "readOnly"
                    ],
                    "metadata": {
                        "inclusion": "available",
                        "selected": true
                    }
                },
                {
                    "breadcrumb": [
                        "properties",
                        "limitExempt"
                    ],
                    "metadata": {
                        "inclusion": "available",
                        "selected": true
                    }
                },
                {
                    "breadcrumb": [
                        "properties",
                        "deleteable"
                    ],
                    "metadata": {
                        "inclusion": "available",
                        "selected": true
                    }
                }
            ]
        }
    ]
}"""

# extracted stream schema
# added key_properties, and type key-value pair
HubSpot_contact_lists_schema_fixed_test = """{

            "type": "SCHEMA",
            "stream": "contact_lists",

            "key_properties": [
                "listId"
            ],

            "schema": {
                "type": "object",
                "properties": {
                    "portalId": {
                        "type": [
                            "null",
                            "integer"
                        ]
                    },
                    "listId": {
                        "type": [
                            "null",
                            "integer"
                        ]
                    },
                    "internalListId": {
                        "type": [
                            "null",
                            "integer"
                        ]
                    },
                    "createdAt": {
                        "type": [
                            "null",
                            "string"
                        ],
                        "format": "date-time"
                    },
                    "updatedAt": {
                        "type": [
                            "null",
                            "string"
                        ],
                        "format": "date-time"
                    },
                    "name": {
                        "type": [
                            "null",
                            "string"
                        ]
                    },
                    "listType": {
                        "type": [
                            "null",
                            "string"
                        ]
                    },
                    "parentId": {
                        "type": [
                            "null",
                            "integer"
                        ]
                    },
                    "authorId": {
                        "type": [
                            "null",
                            "integer"
                        ]
                    },
                    "filters": {
                        "type": [
                            "null",
                            "array"
                        ],
                        "items": {
                            "type": [
                                "null",
                                "array"
                            ],
                            "items": {
                                "type": [
                                    "null",
                                    "object"
                                ],
                                "properties": {
                                    "withinTimeMode": {
                                        "type": [
                                            "null",
                                            "string"
                                        ]
                                    },
                                    "filterFamily": {
                                        "type": [
                                            "null",
                                            "string"
                                        ]
                                    },
                                    "operator": {
                                        "type": [
                                            "null",
                                            "string"
                                        ]
                                    },
                                    "type": {
                                        "type": [
                                            "null",
                                            "string"
                                        ]
                                    },
                                    "property": {
                                        "type": [
                                            "null",
                                            "string"
                                        ]
                                    },
                                    "value": {
                                        "type": [
                                            "null",
                                            "string"
                                        ]
                                    },
                                    "checkPastVersions": {
                                        "type": [
                                            "null",
                                            "boolean"
                                        ]
                                    }
                                }
                            }
                        }
                    },
                    "metaData": {
                        "type": [
                            "null",
                            "object"
                        ],
                        "properties": {
                            "size": {
                                "type": [
                                    "null",
                                    "integer"
                                ]
                            },
                            "lastSizeChangeAt": {
                                "type": [
                                    "null",
                                    "string"
                                ],
                                "format": "date-time"
                            },
                            "processing": {
                                "type": [
                                    "null",
                                    "string"
                                ]
                            },
                            "lastProcessingStateChangeAt": {
                                "type": [
                                    "null",
                                    "string"
                                ],
                                "format": "date-time"
                            },
                            "error": {
                                "type": [
                                    "null",
                                    "string"
                                ]
                            },
                            "listReferencesCount": {
                                "type": [
                                    "null",
                                    "integer"
                                ]
                            },
                            "parentFolderId": {
                                "type": [
                                    "null",
                                    "string"
                                ]
                            }
                        }
                    },
                    "archived": {
                        "type": [
                            "null",
                            "boolean"
                        ]
                    },
                    "dynamic": {
                        "type": [
                            "null",
                            "boolean"
                        ]
                    },
                    "readOnly": {
                        "type": [
                            "null",
                            "boolean"
                        ]
                    },
                    "limitExempt": {
                        "type": [
                            "null",
                            "boolean"
                        ]
                    },
                    "deleteable": {
                        "type": [
                            "null",
                            "boolean"
                        ]
                    }
                }
            },
            "metadata": [
                {
                    "breadcrumb": [],
                    "metadata": {
                        "table-key-properties": [
                            "listId"
                        ],
                        "forced-replication-method": "INCREMENTAL",
                        "valid-replication-keys": [
                            "updatedAt"
                        ],
                        "selected": true
                    }
                },
                {
                    "breadcrumb": [
                        "properties",
                        "portalId"
                    ],
                    "metadata": {
                        "inclusion": "available",
                        "selected": true
                    }
                },
                {
                    "breadcrumb": [
                        "properties",
                        "listId"
                    ],
                    "metadata": {
                        "inclusion": "automatic"
                    }
                },
                {
                    "breadcrumb": [
                        "properties",
                        "internalListId"
                    ],
                    "metadata": {
                        "inclusion": "available",
                        "selected": true
                    }
                },
                {
                    "breadcrumb": [
                        "properties",
                        "createdAt"
                    ],
                    "metadata": {
                        "inclusion": "available",
                        "selected": true
                    }
                },
                {
                    "breadcrumb": [
                        "properties",
                        "updatedAt"
                    ],
                    "metadata": {
                        "inclusion": "automatic"
                    }
                },
                {
                    "breadcrumb": [
                        "properties",
                        "name"
                    ],
                    "metadata": {
                        "inclusion": "available",
                        "selected": true
                    }
                },
                {
                    "breadcrumb": [
                        "properties",
                        "listType"
                    ],
                    "metadata": {
                        "inclusion": "available",
                        "selected": true
                    }
                },
                {
                    "breadcrumb": [
                        "properties",
                        "parentId"
                    ],
                    "metadata": {
                        "inclusion": "available",
                        "selected": true
                    }
                },
                {
                    "breadcrumb": [
                        "properties",
                        "authorId"
                    ],
                    "metadata": {
                        "inclusion": "available",
                        "selected": true
                    }
                },
                {
                    "breadcrumb": [
                        "properties",
                        "filters"
                    ],
                    "metadata": {
                        "inclusion": "available",
                        "selected": true
                    }
                },
                {
                    "breadcrumb": [
                        "properties",
                        "metaData"
                    ],
                    "metadata": {
                        "inclusion": "available",
                        "selected": true
                    }
                },
                {
                    "breadcrumb": [
                        "properties",
                        "archived"
                    ],
                    "metadata": {
                        "inclusion": "available",
                        "selected": true
                    }
                },
                {
                    "breadcrumb": [
                        "properties",
                        "dynamic"
                    ],
                    "metadata": {
                        "inclusion": "available",
                        "selected": true
                    }
                },
                {
                    "breadcrumb": [
                        "properties",
                        "readOnly"
                    ],
                    "metadata": {
                        "inclusion": "available",
                        "selected": true
                    }
                },
                {
                    "breadcrumb": [
                        "properties",
                        "limitExempt"
                    ],
                    "metadata": {
                        "inclusion": "available",
                        "selected": true
                    }
                },
                {
                    "breadcrumb": [
                        "properties",
                        "deleteable"
                    ],
                    "metadata": {
                        "inclusion": "available",
                        "selected": true
                    }
                }
            ]
        }"""

