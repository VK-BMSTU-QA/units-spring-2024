import { applyCategories } from '../applyCategories';
import type { Category, Product } from '../../types';

describe('test applayCategories function', () => {
    it.each([
        {
         products: [
          {id:1, name:"1", description:"1", price:1, category: 'Электроника' as Category} as Product,
          {id:1, name:"1", description:"1", price:1, category: 'Обувь' as Category} as Product,
        ],
         categories: ["Электроника" as Category],
         expected: [{id:1, name:"1", description:"1", price:1, category: 'Электроника' as Category} as Product]
        },
        {
          products: [],
          categories: ["Электроника" as Category],
          expected: []
         },
         {
          products: [],
          categories: [],
          expected: []
         },
      ])('applayCategories($products, $categories)', ({products, categories, expected}) => {
        expect(applyCategories(products, categories)).toStrictEqual(expected);
      });
});
