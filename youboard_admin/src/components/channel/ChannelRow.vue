<template>
  <tr
      v-if="data.item.rank !== null && this.editMode === false"
      @dbclick="editModeOn"
  >
    <td>
      <v-checkbox
          v-model="data.item.selected"
          primary
          hide-details
      ></v-checkbox>
    </td>
    <td class="text-xs-center">{{ data.item.rank }}</td>
    <td class="text-xs-center">{{ data.item.name }}</td>
    <td class="text-xs-center">{{ data.item.category }}</td>
    <td class="text-xs-center">{{ data.item.subscribers }}</td>
    <td class="text-xs-center"><a href="data.item.url">{{ data.item.url }}</a></td>

    <td class="text-xs-center" v-if="data.item.rank !== null">
      <v-btn icon><v-icon small @click="editModeOn()">edit</v-icon></v-btn>
    </td>
  </tr>
</template>

<script>
  export default {
    name: "ChannelRow",
    props: {
      data : Object,
    },
    data () {
      return {
        editMode : false,
      }
    },
    created () {
      this.listenEditModeOff()
    },
    methods : {
      listenEditModeOff () {
        this.$crudEventbus.$on('editModeOff', () => {
          this.editMode = false
        })
      },
      editModeOn () {
        this.$crudEventbus.$emit('editModeOn', this.data.item)
        this.editMode = true
      }
    }
  }
</script>