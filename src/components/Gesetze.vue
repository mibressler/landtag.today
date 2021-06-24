<template>
  <v-row>
          <v-col
            v-for="card in cards"
            :key="card"
            cols="12"
          >
            <v-card>
              <v-subheader>{{ card }}</v-subheader>

              <v-list two-line>
                <template v-for="n in testgesetze">
                  <v-list-item

                    :key="n"
                  >
                    <v-list-item-avatar color="grey darken-1">
                    </v-list-item-avatar>

                    <v-list-item-content>
                      <v-list-item-title>{{n.name }}</v-list-item-title>

                      <v-list-item-subtitle>
                        Näheres zum Gesetz
                      </v-list-item-subtitle>
                    </v-list-item-content>
                  </v-list-item>

                  <v-divider
                    v-if="n !== 6"
                    :key="`divider-${n}`"
                    inset
                  ></v-divider>
                </template>
              </v-list>
            </v-card>
          </v-col>
        </v-row>
</template>

<script>

import json from './assets/gesetze.json'




export default {
        name: "Gesetze",
        data: () => ({
        cards: ['in parlamentarischer Beratung', 'Beratung abgeschlossen'],
        drawer: null,
      // links: [
        //['mdi-inbox-arrow-down', 'Inbox'],
        //['mdi-send', 'Send'],
        //['mdi-delete', 'Trash'],
        //['mdi-alert-octagon', 'Spam'],
     // ],
        return {
                myJson: json
        }
    }),
    
  }

</script>

<style scoped>

</style>