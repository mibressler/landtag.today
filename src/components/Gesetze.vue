<template>
  <v-row>
          <v-col
            cols="12"
          >
            <v-card>
              <v-subheader>in parlamentarischer Beratung</v-subheader>
              <v-list two-line>
                <div v-for="n in gesetzjson" :key="n[0]">
                <template >
                  <v-list-item 

                    :key="n"
                  >
                    <v-list-item-avatar color="grey darken-1">
                    </v-list-item-avatar>

                    <v-list-item-content>
                      <v-list-item-title><a :href="n.mappe" :target="_blank"> {{n.content}} </a> </v-list-item-title>
                        <v-chip-group>
                          <v-chip>{{ n. beratung }}</v-chip>
                          <v-chip>{{ n. status }}</v-chip>
                        </v-chip-group>
                      <v-list-item-subtitle>
                        {{n.title}} vom {{n.date}}
                      </v-list-item-subtitle>
                    </v-list-item-content>
                  </v-list-item>

                 
                </template>
                </div>
              </v-list>
            </v-card>
        
        <v-card>
              <v-subheader>Beratung abgeschlossen</v-subheader>
              <v-list two-line>
                <div v-for="n in gesetzjson" :key="n[0]">
                <template >
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
                }

        },
        methods: {
                activeLaws(arr) {
                        arr = arr.filter(n => n.beratung == "active")
                        return arr
       }
        }
    
  }

</script>

<style scoped>
a {
        text-decoration: none;
}

</style>