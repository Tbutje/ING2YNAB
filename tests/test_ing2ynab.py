import unittest

from ing2ynab.Ing2ynab import Ing2ynab


class TestIng2ynab(unittest.TestCase):
    """
    Create test data like this: print(str(self.data_in).replace(" nan", " float('nan')"))
    """

    def test_single_payment(self):
        """
        Test if single payment is converted correctly
        """
        raw_data = [['20201118', 'GroceryStore', 'NLXXINGB', '', 'BA', 'Af', '5,50', 'Betaalautomaat', 'comment']]
        ing2Ynbab = Ing2ynab.fromlist(data=raw_data)
        ing2Ynbab.convert()

        self.assertEqual(ing2Ynbab.data_out[0].get('Date'), '18/11/2020')
        self.assertEqual(ing2Ynbab.data_out[0].get('Payee'), 'GroceryStore')
        self.assertEqual(ing2Ynbab.data_out[0].get('Category'), '')
        self.assertEqual(ing2Ynbab.data_out[0].get('Memo'), 'comment')
        self.assertEqual(ing2Ynbab.data_out[0].get('Outflow'), '5.50')
        self.assertEqual(ing2Ynbab.data_out[0].get('Inflow'), '')

    def test_bug_2020_12_15(self):
        """
         Turned out it was an error in the to_csv method. Payee was without Caps.
        """
        raw_data = [['20201214', 'Sajoer Juicebar  Cafe ROTTERDAM', 'NLXXINGB', '', 'BA', 'Af', '18,00',
                     'Betaalautomaat',
                     'Pasvolgnr: 001 13-12-2020 10:14 Transactie: J4V604 Term: 6LX4BN Valutadatum: 14-12-2020']]
        ing2Ynbab = Ing2ynab.fromlist(data=raw_data)
        ing2Ynbab.convert()

        self.assertEqual(ing2Ynbab.data_out[0].get('Date'), '14/12/2020')
        self.assertEqual(ing2Ynbab.data_out[0].get('Payee'), 'Sajoer Juicebar  Cafe ROTTERDAM')
        self.assertEqual(ing2Ynbab.data_out[0].get('Category'), '')
        self.assertEqual(ing2Ynbab.data_out[0].get('Memo'),
                         'Pasvolgnr: 001 13-12-2020 10:14 Transactie: J4V604 Term: 6LX4BN Valutadatum: 14-12-2020')
        self.assertEqual(ing2Ynbab.data_out[0].get('Outflow'), '18.00')
        self.assertEqual(ing2Ynbab.data_out[0].get('Inflow'), '')


if __name__ == '__main__':
    unittest.main()
