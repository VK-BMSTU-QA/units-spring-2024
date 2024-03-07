import {updateCategories} from '../updateCategories';
import {Category} from "../../types";

describe('test update Categories function', () => {
    it('should return array with categories', () => {
        let category: Category[] = ['Для дома', 'Одежда']
        expect(updateCategories(category, 'Электроника')).toEqual(['Для дома', 'Одежда', 'Электроника']);
        expect(updateCategories(category, 'Одежда')).toEqual(['Для дома']);
        expect(updateCategories([], 'Одежда')).toEqual(['Одежда']);
        expect(updateCategories(['Одежда'], 'Одежда')).toEqual([]);
    });
});
