**Artist**

`Artist` -|--< `Music`

**Song/Album** belongs to **Artist**

**Artist** has many **Songs/Albums**

<table>
  <th colspan="2" style="text-align:center">Artist</th>
  <tr>
    <td>id</td>
    <td>primary key</td>
  </tr>
  <tr>
    <td>first_name</td>
    <td>string</td>
  </tr>
  <tr>
    <td>last_name</td>
    <td>string</td>
  </tr>
  <tr>
    <td>latest song/album</td>
    <td>string</td>
  </tr>
  <tr>
    <td>release_date</td>
    <td>date</td>
  </tr>
  <tr>
    <td>created_at</td>
    <td>datetime</td>
  </tr>
  <tr>
    <td>updated_at</td>
    <td>datetime</td>
  </tr>
</table>