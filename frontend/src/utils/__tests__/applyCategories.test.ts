import { applyCategories } from '../applyCategories';
import { Category, Product } from '../../types';

describe('test apply categories function', () => {
    it('should return all categories from empty categories', () => {
      let categories: Category[] = ['0' as Category, '1' as Category, '2' as Category]
      let prods: Product[] = []
      for (let i: number = 0; i < 3; i++) {
        prods.push({
          id: i,
          name: "bla bla",
          description: "",
          price: 100,
          priceSymbol:'$',
          imgUrl: '',
          category: categories[i]
        } as Product)
      }
      expect(applyCategories(prods, [])).toStrictEqual(prods)
    });
    it('should return all categories from all categories', () => {
      let categories: Category[] = ['0' as Category, '1' as Category, '2' as Category]
      let prods: Product[] = []
      for (let i: number = 0; i < 3; i++) {
        prods.push({
          id: i,
          name: "bla bla",
          description: "",
          price: 100,
          priceSymbol:'$',
          imgUrl: '',
          category: categories[i]
        } as Product);
      }
      expect(applyCategories(prods, categories)).toStrictEqual(prods);
    });
    it('should return choosen category', () => {
      let categories: Category[] = ['0' as Category, '1' as Category, '2' as Category]
      let prods: Product[] = []
      categories.forEach((category, i) => {
        prods.push({
          id: i,
          name: "bla bla",
          description: "",
          price: 100,
          priceSymbol:'$',
          imgUrl: '',
          category: category
        } as Product)})
      expect(applyCategories(prods, [categories[0]])).toStrictEqual([prods[0]])
    });
});
