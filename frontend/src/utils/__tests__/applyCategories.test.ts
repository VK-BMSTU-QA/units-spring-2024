import { applyCategories } from '../applyCategories';
import { Category, Product } from '../../types';

const generate = () => {
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

    return {categories, prods};
};

describe('test apply categories function', () => {
    it('should return all categories from empty categories', () => {
      const {categories, prods} = generate();
      expect(applyCategories(prods, [])).toStrictEqual(prods)
    });
    it('should return all categories from all categories', () => {
      const {categories, prods} = generate();
      expect(applyCategories(prods, categories)).toStrictEqual(prods);
    });
    it('should return choosen category', () => {
      const {categories, prods} = generate();
      expect(applyCategories(prods, [categories[0]])).toStrictEqual([prods[0]])
    });
});
