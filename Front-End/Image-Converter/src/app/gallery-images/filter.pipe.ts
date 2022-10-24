import { Pipe, PipeTransform } from '@angular/core';
import { TagList } from './gallery-images.component';

@Pipe({
  name: 'filter'
})
export class FilterPipe implements PipeTransform {

  transform(list: TagList[], search: string) {
    if (list.length === 0 || search === '')
      return list;
    else {
      return list.filter((hold) => {
        return (hold.check.toLowerCase().trim().includes(search.toLowerCase().trim()) || hold.imgName.toLowerCase().trim().includes(search.toLowerCase().trim()));
      });
    }
  }

}
