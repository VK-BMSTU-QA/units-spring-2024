import { updateCategories } from '../updateCategories';
import { Category, PriceSymbol } from '../../types'

afterEach(jest.clearAllMocks);
describe('test update Categories function', () => {
    it('should return updated array of Categories', () => {
        expect(updateCategories(['Электроника', 'Одежда', 'Для дома'], 'Электроника')).toEqual(['Одежда', 'Для дома']);
    });

    it('should return updated array of Categories', () => {
        expect(updateCategories(['Одежда', 'Для дома'], 'Электроника')).toStrictEqual(['Одежда', 'Для дома', 'Электроника']);
    });

    it('should return updated array of Categories', () => {
        expect(updateCategories([], 'Для дома')).toStrictEqual(['Для дома']);
    });
    it('should return updated array of Categories', () => {
        expect(updateCategories(['Для дома'], 'Для дома')).toStrictEqual([]);
    });
    it('should return updated array of Categories', () => {
        expect(updateCategories([], 'Одежда')).toStrictEqual(['Одежда']);
    });
});
