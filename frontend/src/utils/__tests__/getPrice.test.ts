import { PriceSymbol } from '../../types';
import { getPrice } from '../getPrice';

describe("test getPrice function", () => {
    it.each([
        {
            price: 100,
            priceSymbol: "$" as PriceSymbol,
            expected: "100 $",
        },
        {
            price: 100123.1,
            priceSymbol: "₽" as PriceSymbol,
            expected: "100\xa0123,1 ₽",
        },
        {
            price: 100000,
            priceSymbol: "₽" as PriceSymbol,
            expected: "100\xa0000 ₽",
        },
        {
            price: 100.12333,
            priceSymbol: "₽" as PriceSymbol,
            expected: "100,123 ₽",
        },
        {
            price: 1/3,
            priceSymbol: "₽" as PriceSymbol,
            expected: "0,333 ₽",
        },
        {
            price: 0,
            priceSymbol: "₽" as PriceSymbol,
            expected: "0 ₽",
        },
        {
            price: NaN,
            priceSymbol: "₽" as PriceSymbol,
            expected: "не\xa0число ₽",
        },
      ])('updateCategories($price, $priceSymbol)', ({price, priceSymbol, expected}) => {
        expect(getPrice(price, priceSymbol)).toStrictEqual(expected);
      });
});
