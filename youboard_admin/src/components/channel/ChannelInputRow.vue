<template>
  <tr class="inputRow" v-if="data.item.id === null || this.editMode === true">
    <td>
      <v-checkbox
          v-model="data.selected"
          primary
          hide-details
      ></v-checkbox>
    </td>
    <td class="text-xs"> </td>
    <td><input v-model="nameInput" type="text"></td>
    <td><input v-model="nameInput" type="text"></td>
    <td><input v-model="nameInput" type="text"></td>
    <td><input v-model="nameInput" type="text"></td>

    <td class="justify-center layout px-0">
      <v-btn
          small icon depressed dark color="black"
          @click="apply()"
      >
        <v-icon>done</v-icon>
      </v-btn>
      <v-btn
          small icon depressed dark color="black"
          @click="cancel()"
      >
        <v-icon>undo</v-icon>
      </v-btn>
    </td>
  </tr>
</template>

<script>
    export default {
        name: "ChannelInputRow",
        props: {
            data: Object,
        },
        data () {
            return {
                editMode : false,
                nameInput : "",
            }
        }
    }

</script>