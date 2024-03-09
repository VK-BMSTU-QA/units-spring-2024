import { Category } from '../../types';
import { updateCategories } from '../updateCategories';

describe('test update categories function', () => {

    const inputCategories : Category[] = [
        'Для дома',
        "Одежда"
    ]

    const inpCategories : Category[] = [
        "Одежда"
    ]

    it('should return changed categories', () => {
        expect(updateCategories(inputCategories, 'Электроника')).toStrictEqual([...inputCategories, 'Электроника']);
    });

    it('should return changed categories', () => {
        expect(updateCategories(inputCategories, 'Одежда')).toStrictEqual([inputCategories[0]]);
    });

    it('should return changed categories', () => {
        expect(updateCategories(inpCategories, 'Одежда')).toStrictEqual([]);
    });
});