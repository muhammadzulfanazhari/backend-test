import json

from http import HTTPStatus
from django.shortcuts import render
from django.http.response import HttpResponse
from django.views import View
from tugas3.bodyweight import helpers, models

class DataAPI(View):
    def get(self, request):
        data = models.BBModel.objects.all()
        return helpers.format_response_list_data(result=data)

    def post(self, request):
        try:
            # get body
            body = json.loads(request.body)

            # validate request
            try:
                helpers.validate_post(body)
            except Exception as e:
                return helpers.format_response(status_code=HTTPStatus.BAD_REQUEST, message="Json format is incorrect")
            
            # check existing data
            data = models.BBModel.objects.filter(tanggal = body["tanggal"]).first()
            if data:
                return helpers.format_response(status_code=HTTPStatus.BAD_REQUEST, message="Tanggal sudah ada")
            
            # create new data
            models.BBModel.objects.create(
                tanggal = body["tanggal"],
                bb_min = body["min"],
                bb_max = body["max"]
            )

            return helpers.format_response(message="Data BB untuk tanggal "+body["tanggal"]+" berhasil disimpan")
        except json.decoder.JSONDecodeError as e:
            return helpers.format_response(status_code=HTTPStatus.BAD_REQUEST, message="Json is not correct")
        except Exception as e:
            return helpers.format_response(status_code=HTTPStatus.INTERNAL_SERVER_ERROR, message="Error is found")


    def put(self, request):
        try:
            # get body
            body = json.loads(request.body)

            # validate request
            try:
                helpers.validate_put(body)
            except Exception as e:
                return helpers.format_response(status_code=HTTPStatus.BAD_REQUEST, message="Json format is incorrect")
            
            # check existing data
            current_data = models.BBModel.objects.filter(tanggal = body["tanggal_lama"]).first()
            if current_data:
                new_data = models.BBModel.objects.filter(tanggal = body["tanggal_baru"]).first()
                if new_data:
                    return helpers.format_response(status_code=HTTPStatus.BAD_REQUEST, message="Tanggal "+body["tanggal_baru"]+" sudah pernah dipakai")
            else:
                return helpers.format_response(status_code=HTTPStatus.BAD_REQUEST, message="Tanggal "+body["tanggal_lama"]+" tidak ditemukan")
            
            # update data data
            current_data.tanggal = body["tanggal_baru"]

            if "min_baru" in body:
                current_data.bb_min = body["min_baru"]
            if "max_baru" in body:
                current_data.bb_max = body["max_baru"]
                
            current_data.save()
            
            return helpers.format_response(message="Data tanggal "+body["tanggal_lama"]+" berhasil diubah")
        except json.decoder.JSONDecodeError as e:
            return helpers.format_response(status_code=HTTPStatus.BAD_REQUEST, message="Json is not correct")
        except Exception as e:
            return helpers.format_response(status_code=HTTPStatus.INTERNAL_SERVER_ERROR, message="Error is found")


    def delete(self, request):
        try:
            # get body
            body = json.loads(request.body)

            # validate request
            try:
                helpers.validate_delete(body)
            except Exception as e:
                return helpers.format_response(status_code=HTTPStatus.BAD_REQUEST, message="Json format is incorrect")
            
            # check existing data
            data = models.BBModel.objects.filter(tanggal = body["tanggal"]).first()
            if not data:
                return helpers.format_response(status_code=HTTPStatus.BAD_REQUEST, message="Tanggal tidak ditemukan")
            
            # delete data data
            data.delete()

            return helpers.format_response(message="Data tanggal "+body["tanggal"]+" berhasil dihapus")
        except json.decoder.JSONDecodeError as e:
            return helpers.format_response(status_code=HTTPStatus.BAD_REQUEST, message="Json is not correct")
        except Exception as e:
            return helpers.format_response(status_code=HTTPStatus.INTERNAL_SERVER_ERROR, message="Error is found")