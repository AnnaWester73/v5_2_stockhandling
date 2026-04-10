Feature: Lagerhållning

  Scenario: Lägga till en valfri produkt
    Given ett tomt lager
    When jag lägger till produkten "Tält" med antal 10
    Then ska produkten finnas i lagret med namn "Tält" och antal 10

  Scenario: Minska antalet av en specifik produkt
    Given att lagret innehåller produkten "Tält" med antal 10
    When jag minskar antalet för produkten "Tält" med 3
    Then ska produkten "Äpple" ha antal 7
