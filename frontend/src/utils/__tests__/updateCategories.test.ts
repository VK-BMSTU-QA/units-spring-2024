import { updateCategories } from '../updateCategories';
import { Category, PriceSymbol } from '../../types'

afterEach(jest.clearAllMocks);
describe('test update Categories function', () => {
    it('should return updated array of Categories', () => {
        expect(updateCategories(['Электроника' as Category, 'Одежда' as Category, 'Для дома' as Category], 'Электроника' as Category)).toEqual(['Одежда' as Category, 'Для дома' as Category]);
        // expect(updateCategories([prod1, prod2], ['Одежда' as Category])).toStrictEqual([]);
        // expect(updateCategories([prod1, prod2, prod3, prod3], ['Одежда' as Category])).toStrictEqual([prod3, prod3]);
        // expect(updateCategories([prod1, prod2, prod3, prod3], [])).toStrictEqual([prod1, prod2, prod3, prod3]);
    });

    it('should return updated array of Categories', () => {
        expect(updateCategories(['Одежда' as Category, 'Для дома' as Category], 'Электроника' as Category)).toStrictEqual(['Одежда' as Category, 'Для дома' as Category, 'Электроника' as Category]);
    });

    it('should return updated array of Categories', () => {
        expect(updateCategories([], 'Для дома' as Category)).toStrictEqual(['Для дома' as Category]);
    });
    it('should return updated array of Categories', () => {
        expect(updateCategories(['Для дома' as Category], 'Для дома' as Category)).toStrictEqual([]);
    });
    it('should return updated array of Categories', () => {
        expect(updateCategories([], 'Одежда' as Category)).toStrictEqual(['Одежда' as Category]);
    });
    // it('', () => {

    // });
});
