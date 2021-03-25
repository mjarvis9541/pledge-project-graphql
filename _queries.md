# Show all actions, questions and answers
- will show selectAnswers as "[]" if we expect a numeric response to the question.


## Query:
query showAllActionsAssociatedQAs {
  actions {
    id
    title
    version
    questions {
      questionNumber
      questionText
      selectAnswers {
        response
        value
      }
    }
  }
}

## Result:
{
  "data": {
    "actions": [
      {
        "id": "1",
        "title": "Veg Out",
        "version": 1,
        "questions": [
          {
            "questionNumber": "1 of 2",
            "questionText": "At the moment, I munch on CURRENT_MEALS meaty meals each week.",
            "selectAnswers": []
          },
          {
            "questionNumber": "2 of 2",
            "questionText": "For the next two months, I pledge to go veg for VEGGIE_MEALS extra meals each week.",
            "selectAnswers": [
              {
                "response": "1 to 5",
                "value": 2.5
              },
              {
                "response": "6 to 10",
                "value": 3
              },
              {
                "response": "10+",
                "value": 3.5
              }
            ]
          }
        ]
      },
      {
        "id": "2",
        "title": "Clean Bills",
        "version": 1,
        "questions": [
          {
            "questionNumber": "1 of 3",
            "questionText": "Within the next two months, I pledge to switch from my current energy supplier – which is ENERGY_SUPPLIER – to a green energy supplier.",
            "selectAnswers": [
              {
                "response": "Bog Standard",
                "value": 0.5
              },
              {
                "response": "A Great Green Tariff",
                "value": 0
              }
            ]
          },
          {
            "questionNumber": "2 of 3",
            "questionText": "NUMBER_OF_PEOPLE people live in our home.",
            "selectAnswers": []
          },
          {
            "questionNumber": "3 of 3",
            "questionText": "My house is mainly heated by HEATING_SOURCE.",
            "selectAnswers": [
              {
                "response": "Gas or Oil",
                "value": 5
              },
              {
                "response": "Electricity",
                "value": 3
              }
            ]
          }
        ]
      }
    ]
  }
}

# Find all pledges by users, actions, date pledged, questions and answers:
## Query:
query findAllPledgesByAllUsers {
  users {
    username
    pledges {
      date
      action {
        title
        version
        questions {
          questionNumber
          questionText
          answers {
            responseSelect {
              response
            }
            responseNumber
          }
        }
      }
    }
  }
}

## Result:
{
  "data": {
    "users": [
      {
        "username": "admin",
        "pledges": [
          {
            "date": "2021-03-25T22:00:33.363429+00:00",
            "action": {
              "title": "Veg Out",
              "version": 1,
              "questions": [
                {
                  "questionNumber": "1 of 2",
                  "questionText": "At the moment, I munch on CURRENT_MEALS meaty meals each week.",
                  "answers": [
                    {
                      "responseSelect": null,
                      "responseNumber": 32
                    },
                    {
                      "responseSelect": null,
                      "responseNumber": 18
                    }
                  ]
                },
                {
                  "questionNumber": "2 of 2",
                  "questionText": "For the next two months, I pledge to go veg for VEGGIE_MEALS extra meals each week.",
                  "answers": [
                    {
                      "responseSelect": {
                        "response": "10+"
                      },
                      "responseNumber": null
                    },
                    {
                      "responseSelect": {
                        "response": "6 to 10"
                      },
                      "responseNumber": null
                    }
                  ]
                }
              ]
            }
          }
        ]
      },
      {
        "username": "freddy",
        "pledges": [
          {
            "date": "2021-03-25T22:47:29+00:00",
            "action": {
              "title": "Veg Out",
              "version": 1,
              "questions": [
                {
                  "questionNumber": "1 of 2",
                  "questionText": "At the moment, I munch on CURRENT_MEALS meaty meals each week.",
                  "answers": [
                    {
                      "responseSelect": null,
                      "responseNumber": 32
                    },
                    {
                      "responseSelect": null,
                      "responseNumber": 18
                    }
                  ]
                },
                {
                  "questionNumber": "2 of 2",
                  "questionText": "For the next two months, I pledge to go veg for VEGGIE_MEALS extra meals each week.",
                  "answers": [
                    {
                      "responseSelect": {
                        "response": "10+"
                      },
                      "responseNumber": null
                    },
                    {
                      "responseSelect": {
                        "response": "6 to 10"
                      },
                      "responseNumber": null
                    }
                  ]
                }
              ]
            }
          }
        ]
      },
      {
        "username": "alice",
        "pledges": []
      },
      {
        "username": "francis",
        "pledges": []
      },
      {
        "username": "anastasia",
        "pledges": [
          {
            "date": "2021-03-25T23:03:21+00:00",
            "action": {
              "title": "Clean Bills",
              "version": 1,
              "questions": [
                {
                  "questionNumber": "1 of 3",
                  "questionText": "Within the next two months, I pledge to switch from my current energy supplier – which is ENERGY_SUPPLIER – to a green energy supplier.",
                  "answers": [
                    {
                      "responseSelect": {
                        "response": "Bog Standard"
                      },
                      "responseNumber": null
                    }
                  ]
                },
                {
                  "questionNumber": "2 of 3",
                  "questionText": "NUMBER_OF_PEOPLE people live in our home.",
                  "answers": [
                    {
                      "responseSelect": null,
                      "responseNumber": 4
                    }
                  ]
                },
                {
                  "questionNumber": "3 of 3",
                  "questionText": "My house is mainly heated by HEATING_SOURCE.",
                  "answers": [
                    {
                      "responseSelect": {
                        "response": "Gas or Oil"
                      },
                      "responseNumber": null
                    }
                  ]
                }
              ]
            }
          }
        ]
      }
    ]
  }
}