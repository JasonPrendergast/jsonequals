Feature: test cases jsonequal class
  #background will run before every scenario
  Background: Create context json string
    Given I create new context json string

  Scenario Outline: "<key>" and "<value>"
  Scenario: equal date
    Given I have a keypair 'value1' '2017-06-16T21:36:48.362Z'
    And I have a keypair 'value2' '2017-06-16T21:36:48.362Z'
    And I have a keypair 'description' 'equal date objects'
    And I have last keypair 'equal' 'True'
#    Then I should see 'True'

  Examples:
		| key         | value                   |
		| value1      | 2017-06-16T21:36:48.362Z|
		| value2      | 2017-06-16T21:36:48.362Z|
		| description | equal date objects      |
		| equal       | True                    |



