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
                <div v-for="n in gesetzjson" :key="n[0]">
                <template v-if="n.beratung == 'aktiv'" >
                  <v-list-item 

                    :key="n"
                  >
                    <v-list-item-avatar color="grey darken-1">
                    </v-list-item-avatar>

                    <v-list-item-content>
                      <v-list-item-title>{{n.content}}</v-list-item-title>

                      <v-list-item-subtitle>
                        {{n.title}} vom {{n.date}}
                      </v-list-item-subtitle>
                    </v-list-item-content>
                  </v-list-item>

                  <v-divider
                    v-if="n !== 6"
                    :key="`divider-${n}`"
                    inset
                  ></v-divider>
                </template>
                </div>
              </v-list>
            </v-card>
          </v-col>
        </v-row>
</template>

<script>

import json from './gesetze.json';


const gesetzjson = JSON.parse(JSON.stringify(json));

const aktivegs = [];
for (let i in gesetzjson) {
        aktivegs[i] = gesetzjson.i
}
alert(gesetzjson)

console.log(gesetzjson[0].title);

export default {
        name: "Gesetze",
        data() {
                return {
                        cards: ['in parlamentarischer Beratung', 'Beratung abgeschlossen'],
                        drawer: null,
                        // links: [
                         //['mdi-inbox-arrow-down', 'Inbox'],
                         //['mdi-send', 'Send'],
                        //['mdi-delete', 'Trash'],
                          //['mdi-alert-octagon', 'Spam'],
                         // ],
                         gesetzjson: gesetzjson,
                        aktivegs: aktivegs,
                }

    },
    
  }

</script>

<style scoped>

</style>