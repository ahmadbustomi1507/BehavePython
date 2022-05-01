Feature: Testing aja
  Background: nama backgroundnya
    Given ceritanya gw ambil datanya dsini ngab
          | data_1 | data_2|
          |.       | .     |

  Scenario: Scenario 1 _ ambil data dari background ngab
      Given dsini dipake <data_1>
      When user using <data_2>
      Then  user success

  Scenario: Scenario 2 _ ambil data dari background ngab
      Given dsini dipake <data_1>
      When user using <data_2>
      Then  user success