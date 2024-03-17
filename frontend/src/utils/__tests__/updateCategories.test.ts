import { Category } from '../../types';
import { updateCategories } from '../updateCategories';

describe('test update categories function', () => {

    const inputTwoCategories : Category[] = [
        'Для дома',
        "Одежда"
    ]

    const inputOneCategorie : Category[] = [
        "Одежда"
    ]

    it('should return input categories and one added category', () => {
        expect(updateCategories(inputTwoCategories, 'Электроника')).toStrictEqual([...inputTwoCategories, 'Электроника']);
    });

    it('should return categories without one mentioned in input list', () => {
        expect(updateCategories(inputTwoCategories, 'Одежда')).toStrictEqual([inputTwoCategories[0]]);
    });

    it('should return nothing from list with one category which mentioned in input data', () => {
        expect(updateCategories(inputOneCategorie, 'Одежда')).toStrictEqual([]);
    });
});
