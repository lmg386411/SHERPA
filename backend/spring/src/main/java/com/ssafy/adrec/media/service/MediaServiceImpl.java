package com.ssafy.adrec.media.service;

import com.ssafy.adrec.media.Company;
import com.ssafy.adrec.media.MediaSub;
import com.ssafy.adrec.media.MediaType;
import com.ssafy.adrec.media.MediaTypes;
import com.ssafy.adrec.media.repository.CompanyRepository;
import com.ssafy.adrec.media.repository.MediaSubRepository;
import com.ssafy.adrec.media.repository.MediaTypeRepository;
import com.ssafy.adrec.media.response.CompanyGetRes;
import com.ssafy.adrec.media.response.MediaSubGetRes;
import com.ssafy.adrec.media.response.MediaTypeGetRes;
import com.ssafy.adrec.member.service.MemberServiceImpl;
import lombok.RequiredArgsConstructor;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.List;
import java.util.Objects;
import java.util.Optional;

@Service
@RequiredArgsConstructor
public class MediaServiceImpl implements MediaService{
    public static final Logger logger = LoggerFactory.getLogger(MemberServiceImpl.class);

    private final MediaTypeRepository mediaTypeRepository;
    private final MediaSubRepository mediaSubRepository;
    private final CompanyRepository companyRepository;

    @Override
    public List<MediaTypeGetRes> getMediaTypeList(MediaTypes mediaTypes, Long id) {
        List<MediaTypeGetRes> list = new ArrayList<>();

        if (Objects.requireNonNull(mediaTypes) == MediaTypes.MEDIATYPE) {
            List<MediaType> mediaTypeList = mediaTypeRepository.findAll();
            for (MediaType mediaType : mediaTypeList) {
                list.add(new MediaTypeGetRes(mediaType.getId(), mediaType.getLarge(), mediaType.getMedium()));
            }
        }

        return list;
    }

    @Override
    public List<MediaSubGetRes> getMediaSubList(MediaTypes mediaTypes, Long id) {
        List<MediaSubGetRes> list = new ArrayList<>();

        if (Objects.requireNonNull(mediaTypes) == MediaTypes.MEDIASUB) {
            List<MediaSub> mediaSubList = mediaSubRepository.findAllByMediaType_Id(id);
            for (MediaSub mediaSub : mediaSubList) {
                list.add(new MediaSubGetRes(mediaSub.getId(), mediaSub.getSmall()));
            }
        }

        return list;
    }

    @Override
    public List<CompanyGetRes> getCompanyList(Long mediaTypeId, Long mediaSubId){
        List<CompanyGetRes> list = new ArrayList<>();

        if(1 <= mediaTypeId && mediaTypeId <= 5){
            List<Company> companyList = companyRepository.findAllByMediaType_Id(mediaTypeId);
            for (Company company : companyList){
                list.add(new CompanyGetRes(company.getImg(), company.getName(), company.getUrl()));
            }
        }else{
            List<Company> companyList = companyRepository.findAllByMediaType_IdAndMediaSub_Id(mediaTypeId, mediaSubId);
            for (Company company : companyList){
                list.add(new CompanyGetRes(company.getImg(), company.getName(), company.getUrl()));
            }
        }

        return list;
    }

    @Override
    public MediaType getMediaType(Long id){

        Optional<MediaType> mediaType = mediaTypeRepository.findById(id);
        return mediaType.orElse(null);

    }

    @Override
    public MediaSub getMediaSub(Long id){

        Optional<MediaSub> mediaSub = mediaSubRepository.findById(id);
        return mediaSub.orElse(null);

    }

}
